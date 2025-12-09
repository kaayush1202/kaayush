from django.urls import path
from .views import *
urlpatterns =[
    path('products/',product_list,name="product_list"),
    path('product/add-new/',create_product,name="create_product"),
    path('brand/add-new/',create_brand,name="create_brand"),
    path('brands/', brand_list_view, name='brand_list'),  
    path('brands/<int:id>/', brand_details_view, name='brand_detail'),
    path('category/',create_category,name="create_category"),
    path('product/update/<int:id>/',update_product,name="update_product"),
    path('product/delete/<int:id>/',delete_product,name="delete_product"),
    path('product/details/<int:pk>/',product_details,name="product_details"),
    path('search/',search_all, name='search_products'),
    
]
