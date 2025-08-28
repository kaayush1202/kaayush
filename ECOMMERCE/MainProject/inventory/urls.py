from django.urls import path
from .views import *
urlpatterns =[
    path('products/',product_list,name="product_list"),
    path('product/add-new/',create_product,name="create_product"),
    path('product/update/<int:id>/',update_product,name="update_product"),
    path('product/delete/<int:id>/',delete_product,name="delete_product"),
    path('product/details/<int:pk>/',product_details,name="product_details"),
]
