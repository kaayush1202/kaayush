from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductCreateForm
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'home.html',context)
 
def create_product(request):
    form = ProductCreateForm()
    if request.method == "GET":
        return render(request,'inventory/product_create.html',{'form':form})
    elif request.method == "POST":
        form = ProductCreateForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('product_list')
        else:
            return render(request,'inventory/product_create.html',{'form':form})
    else:
        return render(request,'inventory/product_create.html',{'form':form})
    
def product_details(request,pk):
    product = get_object_or_404(Product,id=pk)
    context = {
        'product':product
    }
    return render(request,"inventory/product_details.html",context)

def update_product(request,id):
    product=get_object_or_404(Product,id=id)
    form=ProductCreateForm(instance=product)
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_details', id=product.id)

    return render(request, 'inventory/product_update.html', {'form': form})
def delete_product(request,id):
    product=get_object_or_404(Product,id=id)
    if request.method == "GET":
        return render(request,'inventory/confirm_delete.html',{'product':product})
    elif request.method == "POST":
        product.delete()
    return redirect('product_list')