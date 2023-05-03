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

    #Файловый дескриптор в памяти
    bio = BytesIO()

    with ExcelWriter(bio, mode="w") as writer:
        df.to_excel(
            writer,
            engine='xlsxwriter',
            index=False,
            sheet_name="Sheet1"
        )

    bio.seek(0)
    workbook = bio.read()

    response = HttpResponse(workbook, content_type='application/xlsx')
    filename = "report"
    response['Content-Disposition'] = f"attachment; filename={filename}.xlsx"

    return response


def get_orders_on_day_to_xlsx(request):

    def validation_date(date):
        format_date = "%Y-%m-%d"

        try:
            date = datetime.strptime(date, format_date)
            return date.strftime(format_date)
        except ValueError:
            return None

    def count_dishes(dishes_list):

        dishes_set = set()

        for dish in dishes_list:
            dishes_set.add(dish)

        print(dishes_set)

    print(request.GET)
    day_date_str = request.GET.get('date', '')
    day_date_valid_str = validation_date(day_date_str)
    data_json = requests.get("http://127.0.0.1:8000/api/v1/orders/").json()

    df = DataFrame.from_dict(data_json)
    df = df[df['date'] == day_date_valid_str]

    dishes_list = df.groupby(['date'])['dishes'].sum().iloc[0]
    #count = count_dishes(dishes_list)
    df_dishes = DataFrame(data=dishes_list)
    df_dishes = df_dishes.groupby(['title', 'price'])['price'].agg(['sum','count'])
    #df_dishes = pd.concat([df_dishes, pd.Series(['Итоговая сумма', df_dishes.groupby('sum').sum()])])
    print(df_dishes)

    bio = BytesIO()

    with ExcelWriter(bio, mode="w") as writer:
        df_dishes.to_excel(
            writer,
            engine='xlsxwriter',
            sheet_name="Sheet1"
        )

    bio.seek(0)
    workbook = bio.read()

    response = HttpResponse(workbook, content_type='application/xlsx')
    filename = "report"
    response['Content-Disposition'] = f"attachment; filename={filename}.xlsx"

    return response


class OrderApiList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
