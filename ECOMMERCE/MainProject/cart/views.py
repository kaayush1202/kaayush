from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from accounts.models import User
from .models import Cart
from inventory.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_cart(request,id):
    product = get_object_or_404(Product,id=id)
    cart = Cart.objects.filter(user=request.user, product=product).first()
    print(cart)
    if cart:
        cart.quantity +=1
        cart.save()
    else:
        cart=Cart.objects.create(user = request.user,product=product,quantity = 1)
    context ={
    'cart_items':Cart.objects.filter(user=request.user)
    }
    return render(request,'cart.html',context)

@login_required
def showcart(request):
    
    cart_items=Cart.objects.filter(user=request.user)
    context={
        'cart_items':cart_items
    }
    return render(request,'cart.html',context)

@login_required 
def del_cart(request, product_id):
    cart_item = get_object_or_404(Cart, product__id=product_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('showcart')