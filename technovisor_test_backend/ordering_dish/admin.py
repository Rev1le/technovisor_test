from django.contrib import admin

from .models import Worker, Dish, Order


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_filter = ('price',)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'display_dishes')
    list_filter = ('date', 'worker')
