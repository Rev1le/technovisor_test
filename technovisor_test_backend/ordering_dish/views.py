from django.http import HttpResponse
from django.core import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Worker, Dish, Order
from .serializers import OrderSerializer


def get_workers_list(request):
    workers_list = serializers.serialize("json", Worker.objects.all())
    return HttpResponse(workers_list, content_type="application/json")


def get_dishes_list(request):
    dishes_list = serializers.serialize("json", Dish.objects.all())
    return HttpResponse(dishes_list, content_type="application/json")


class OrderApiList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderApiView(APIView):

    def get(self, request):
        orders_lst = Order.objects.all()
        serialize = OrderSerializer(data=orders_lst, many=True)
        serialize.is_valid(raise_exception=True)

        return Response({
            'orders': serialize.data()
        })

    def post(self, request):
        print("Request: ==>", request.data)

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'order': serializer.data})
