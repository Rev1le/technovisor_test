from django.contrib import admin
from django.urls import path, include

from ordering_dish.views import (
    get_workers_list,
    get_dishes_list,
    OrderApiList,
    get_orders_to_xlsx,
    get_dishes_on_day_to_xlsx
)


api_urls = [
    path('workers/', get_workers_list),
    path('dishes/', get_dishes_list),
    path('orders/', OrderApiList.as_view()),
    path('create_order/', OrderApiList.as_view()),
    path('orders_on_timedelta_xlsx/', get_orders_to_xlsx),
    path('dishes_on_day_xlsx/', get_dishes_on_day_to_xlsx),
]


urlpatterns = [
    path('api/v1/', include(api_urls)),
    path('admin/', admin.site.urls),
]
