from rest_framework import serializers

from .models import Order, Worker, Dish

#
# class WorkerSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=128)
#
#
# class DishSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=128)
#     composition = serializers.CharField()
#     price = serializers.FloatField()
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     #date = serializers.DateField()
#     #worker = serializers.IntegerField()
#     #worker_name = serializers.ReadOnlyField()
#
#     class Meta:
#         model = Order
#         fields = ['date', 'worker']
#
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         print('\n\n\n\n\n', response)
#         response['date'] = instance.date
#         response['worker'] = WorkerSerializer(instance.worker).data
#         return response
#
#     def create(self, validated_data):
#         return Order(**validated_data)
#
#
# class DishesOrderSerializer(serializers.ModelSerializer):
#     order = serializers.PrimaryKeyRelatedField(many=True)
#     dish = serializers.PrimaryKeyRelatedField(many=True)
#
#     class Meta:
#         model = DishOrder
#         fields = ['order', 'dish']
#
#     # def to_representation(self, instance):
#     #     response = super().to_representation(instance)
#     #     print("\n\n\n\n\n\n\n\n\nInstance ===> ", str(instance))
#     #     response['order'] = OrderSerializer(data=instance.order).data
#     #     response['dish'] = Dish.objects.get(instance.dish)
#     #     return response
#
#     def create(self, validated_data):
#         #dishes_ids = validated_data.pop("dish")
#         #order = Order.objects.create(**validated_data)
#         #dishes = Dish.objects.get(dishes_ids)
#         #DishOrder.objects.create(many=True)
#
#         return None
#         #dishes_ids = validated_data.pop("dish")
#
#         #dishes = Dish.objects.get(dishes_ids)
#         #order = Order.objects.create(**validated_data)
#
#         #print(dishes, order)
#
#         #return DishOrder.objects.create(many=True, dish=dishes, order=order)
#
# # return DishOrder(**validated_data)


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name']
        model = Worker


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ['title', 'composition', 'price']


class OrderDishesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['date', 'worker', 'dishes']

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
