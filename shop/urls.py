from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_success/', lambda request: None, name='order_success'),
]