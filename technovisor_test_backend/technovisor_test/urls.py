from django.contrib import admin
from django.urls import path, include

from ordering_dish.views import (
    get_workers_list,
    get_dishes_list,
    OrderDishesApiView
)


api_urls = [
    path('workers/', get_workers_list),
    path('dishes/', get_dishes_list),
    path('create_order/', OrderDishesApiView.as_view())
]


urlpatterns = [
    path('api/v1/', include(api_urls)),
    path('admin/', admin.site.urls),
]
