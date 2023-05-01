from rest_framework import serializers

from .models import Order, Worker, Dish


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = Worker


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['title', 'composition', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'date', 'worker', 'dishes']

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['worker'] = WorkerSerializer(instance.worker).data
        response['dishes'] = DishSerializer(instance.dishes, many=True).data

        return response

    def create(self, validated_data):
        dishes_ids = validated_data.pop('dishes', [])

        new_order = Order.objects.create(**validated_data)
        new_order.dishes.set(dishes_ids)
        new_order.save()

        return new_order
