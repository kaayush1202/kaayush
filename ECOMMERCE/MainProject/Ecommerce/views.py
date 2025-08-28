from django.shortcuts import render,HttpResponse
from inventory.models import Product
def home(request):
    products =  Product.objects.all()
    context = {
        'products' : products
    }
    return render(request,'home.html',context)