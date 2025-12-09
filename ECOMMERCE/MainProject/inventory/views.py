from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Brand,Category
from .forms import ProductCreateForm,BrandCreateForm,CategoryCreateForm
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'home.html',context)
# def brand_list(request):
#     brand = Brand.objects.all()
#     context = {
#         'brand':brand
#     }
#     return render(request,'brandfor.html',context)
# def category_list(request):
#     category = Category.objects.all()
#     context = {
#         'category':category
#     }
#     return render(request,'brandfor.html',context)
def brand_list_view(request):
    brands = Brand.objects.all()
    return render(request, 'inventory/brandfor.html', {'brands': brands})
def brand_details_view(request, id):
    brand = get_object_or_404(Brand, id=id)
    return render(request, 'inventory/brands_detail.html', {'brand': brand})

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

def create_brand(request):
    if request.method == "POST":
        form = BrandCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = BrandCreateForm()
    return render(request, 'inventory/brandcreate.html', {'form': form})

def create_category(request):
    form = CategoryCreateForm()
    if request.method == "GET":
        return render(request,'inventory/category_c.html',{'form':form})
    elif request.method == "POST":
        form = CategoryCreateForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('product_list')
        else:
            return render(request,'inventory/category_c.html',{'form':form})
    else:
        return render(request,'inventory/category_c.html',{'form':form})
    

from django.db.models import Q
from django.shortcuts import render
from .models import Product, Brand, Category

def search_all(request):
    query = request.GET.get('q', '').strip()

    product_results = []
    brand_results = []
    category_results = []
    no_results = False

    if query:
        words = query.split()  # split into multiple words

        q_objects = Q()
        for word in words:
            q_objects |= Q(product_name__icontains=word)
            q_objects |= Q(product_des__icontains=word)
            q_objects |= Q(brand__name__icontains=word)
            q_objects |= Q(category__name__icontains=word)

        product_results = Product.objects.filter(q_objects).distinct()
        brand_results = Brand.objects.filter(name__icontains=query).distinct()
        category_results = Category.objects.filter(name__icontains=query).distinct()

        if not product_results and not brand_results and not category_results:
            no_results = True

    context = {
        'query': query,
        'product_results': product_results,
        'brand_results': brand_results,
        'category_results': category_results,
        'no_results': no_results,
    }

    return render(request, "inventory/search_all_results.html", context)
