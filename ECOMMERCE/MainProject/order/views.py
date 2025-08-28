import razorpay
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from uuid import uuid4
from .forms import OrderForm
from accounts.models import User
from cart.models import Cart
from inventory.models import Product
from order.models import Order
from orderdetail.models import OrderDetail
from django.conf import settings
# Create your views here.
@login_required
def checkout(request):
    if request.method == "GET":
        address = request.user.address.all()
        if len(address)==0:
            return redirect("add_address")
        else:
            form = OrderForm()
            return render(request,'orders/checkout.html',{'form':form})
    elif request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order_obj = form.save(commit=False)
            order_obj.user = request.user
            order_obj.uuid = uuid4()
            order_obj.save()
            cust_obj = User.objects.get(username=request.user)
            # cust_obj = Customer.objects.get(user=user_obj.id)
            cart_obj = Cart.objects.filter(user = cust_obj )
            total=0
            for item in cart_obj:
                price= Product.objects.get(id = item.product.id).price
                total = total + (item.quantity * price)
                order_item_obj = OrderDetail(order=order_obj,product=item.product,quantity = item.quantity,price=price)
                order_item_obj.save()
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
            order_obj.total = int(total*100)
            data = { "amount": order_obj.total, "currency": "INR", "receipt": str(order_obj.uuid)}
            payment = client.order.create(data=data)
            order_obj.payment_id = payment.get('id')       
            order_obj.save() #Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            context = {
                'order':order_obj,
                'total':total,
                'payment':payment   
            }
            return render(request,'payments/makepayment.html',context)


