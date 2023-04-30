from django.http import HttpResponse
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Worker, Dish, Order
from .serializers import OrderDishesSerializer


def get_workers_list(request):
    workers_list = serializers.serialize("json", Worker.objects.all())
    return HttpResponse(workers_list, content_type="application/json")


def get_dishes_list(request):
    dishes_list = serializers.serialize("json", Dish.objects.all())
    return HttpResponse(dishes_list, content_type="application/json")


class OrderDishesApiView(APIView):

    def post(self, request):
        print("Request: ==>", request.data)

        serializer = OrderDishesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'order': serializer.data})
