from datetime import datetime, timedelta
from collections import Counter
from io import BytesIO

from django.http import HttpResponse
from django.core import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from pandas import DataFrame, ExcelWriter
import pandas as pd
import requests

from .models import Worker, Dish, Order
from .serializers import OrderSerializer


def create_xlsx_reader_for_df(df):
    bio = BytesIO()

    with ExcelWriter(bio, mode="w") as writer:
        df.to_excel(
            writer,
            engine='xlsxwriter',
            index=False,
            sheet_name="Sheet1"
        )

    bio.seek(0)
    return bio


def get_workers_list(request):
    workers_list = serializers.serialize("json", Worker.objects.all())
    return HttpResponse(workers_list, content_type="application/json")


def get_dishes_list(request):
    dishes_list = serializers.serialize("json", Dish.objects.all())
    return HttpResponse(dishes_list, content_type="application/json")


def get_orders_to_xlsx(request):

    def dishes_to_str(dishes):
        dishes_title_map = map(lambda dish: dish['title'], dishes)
        return ", ".join(dishes_title_map)

    time_delta_dict = {
        'day': timedelta(days=1),
        'month': timedelta(weeks=4),
        'year': timedelta(weeks=4*12),
        '': datetime.fromtimestamp(0)
    }

    req_time_delta = request.GET.get('delta', '')
    time_delta = time_delta_dict[req_time_delta]

    data_json = requests.get("http://127.0.0.1:8000/api/v1/orders/").json()
    df = DataFrame(data=data_json)

    date_today = datetime.today()

    # today - (today - 1970)
    prev_month = date_today - (date_today - time_delta)
    prev_time = prev_month.replace(day=1)

    df['date'] = pd.to_datetime(df['date'])
    df = df[df["date"].between(prev_time, date_today, inclusive="both")]

    df["worker"] = df["worker"].transform(lambda worker: worker["name"])
    df["dishes"] = df["dishes"].transform(dishes_to_str)

    del df['id']
    df = df.rename(
        columns={
            "date": "Дата заказа",
            "worker": "Работник",
            "dishes": "Блюда"
        },
        errors="raise"
    )
    df = df.sort_values(by=['Дата заказа'])

    bio = create_xlsx_reader_for_df(df)
    workbook = bio.read()

    response = HttpResponse(workbook, content_type='application/xlsx')
    filename = "report_orders_on_timedelta"
    response['Content-Disposition'] = f"attachment; filename={filename}.xlsx"

    return response


def get_dishes_on_day_to_xlsx(request):

    def validation_date(date):
        format_date = "%Y-%m-%d"

        try:
            date = datetime.strptime(date, format_date)
            return date.strftime(format_date)
        except ValueError:
            return None

    print(request.GET)
    day_date_str = request.GET.get('date', '')
    day_date_valid_str = validation_date(day_date_str)
    data_json = requests.get("http://127.0.0.1:8000/api/v1/orders/").json()

    df = DataFrame.from_dict(data_json)
    df = df[df['date'] == day_date_valid_str]
    try:
        dishes_list = df.groupby(['date'])['dishes'].sum().iloc[0]
    except IndexError:
        return HttpResponse("None", content_type='application/json')

    df_dishes = DataFrame(data=dishes_list)
    df_dishes = df_dishes.groupby(['title', 'price'])['price'].agg(['sum','count'])

    # Создание итоговой суммы и запись её в отедльный столбец
    #df_dishes = pd.concat([df_dishes, pd.Series(['Итоговая сумма', df_dishes.groupby('sum').sum()])])

    df_dishes.reset_index(inplace=True)
    df_dishes = df_dishes.rename(
        columns={
            "title": "Название блюда",
            "price": "Цена блюда",
            "sum": "Сумма закупки",
            "count": "Кол-во"
        },
        errors="raise"
    )
    print(df_dishes)

    bio = create_xlsx_reader_for_df(df_dishes)

    workbook = bio.read()

    response = HttpResponse(workbook, content_type='application/xlsx')
    filename = "report_dishes_on_date"
    response['Content-Disposition'] = f"attachment; filename={filename}.xlsx"

    return response


class OrderApiList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
