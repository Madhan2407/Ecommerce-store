from django.urls import path
from . import views

app_name='cart'

urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove-one/<int:product_id>/',views.cart_remove_one,name='cart_remove_one'),
    path('remove-item/<int:product_id>/',views.cart_remove_item,name='cart_remove_item'),
    path('',views.cart_detail,name='cart_detail'),
    ]