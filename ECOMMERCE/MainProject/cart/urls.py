from django.urls import path
from .views import *
urlpatterns =[
    path('cart/<int:id>/',add_cart,name="add_to_cart"),
    path('cart/',showcart,name="showcart"),
    path('cart/delete/<int:product_id>/', del_cart, name='del_cart'),
]