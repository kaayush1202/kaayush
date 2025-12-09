from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm
from .forms import AddressForm
from django.core.mail import send_mail
from random import randint
from .models import User
from order.models import Order
from django.contrib.auth.decorators import login_required
from .models import Address
# Create your views here.
def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {
            'form' : form
        }
        return render(request,"register.html",context)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        context = {
            'form' : form
        }
        if form.is_valid():
            request.session['otp'] = randint(1000,9999)
            print(request.session['otp'])
            send_mail(
                        subject='Test Email',
                        message=f'Hello, this is a test email from Django!{request.session["otp"]} ',
                        from_email='sanataniaayushjha112@gmail.com',
                        recipient_list=[form.cleaned_data.get('email')],
                        fail_silently=False,
    )
            request.session['username'] = form.cleaned_data.get('username')
            form.save()
            return render(request,"email_verify.html")
        else:
            return render(request,"register.html",context)

def email_verify(request):
    if request.method =="POST":
        print( request.session['otp'] , request.POST.get('otp',0))
        if int(request.session['otp']) == int(request.POST.get('otp',0)):
            user = User.objects.get(username=request.session['username'])
            user.verified = True
            user.save()
            return redirect('/')
        else:
            return render(request,"email_verify.html")
    else:
        return redirect('/')
# def user_list(request):
#     users = User.objects.all()
#     context = {
#         'users':users
#     }
#     return render(request,'for.html',context)
# def user_details(request,id):
#     user = get_object_or_404(User,id=id)
    
#     user=Order.objects.filter(user=user).first()
#     print(user)
#     context = {
#         'user':user 
#     }
#     return render(request,'id.html',context)

from django.contrib.auth import login,authenticate,logout
from .forms import LoginForm
def my_login(request):
    form = LoginForm()
    if request.method == "GET":
        return render(request,'accounts/login.html',{'form':form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username = username,password = password)
            if user:
                login(request,user)
                return redirect('/')
    return redirect('login')
def log_out(request):
    form= LoginForm()
    if request.method == "GET":
        return render(request,'accounts/login.html',{'form':form})
    elif request.method == "POST":
        logout(request)
        return redirect('form')
@login_required
def add_address(request):
    form= AddressForm()
    if request.method == "GET":
        return render(request,'addressform.html',{'form':form})
    elif request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid(): 
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('add_address')
        else:
            return render(request,'addressform.html',{'form':form})
    else:
        return render(request,'addressform.html',{'form':form})
@login_required
def show_address(request):
    addresses = Address.objects.filter(user=request.user)
    context = {
        'addresses': addresses
    }
    return render(request, 'show_address.html', context)
@login_required
def profilepage(request,pk):
    user=User.objects.get(id=pk)
    context={
        'user':user
    }
    return render(request,'profilepage.html',context)

from .forms import edit_profile_form
@login_required
def edit_profile(request,pk):
    user=get_object_or_404(User,id=pk)
    if request.user != user:
        return redirect('profile_page', pk=user.id)

    if request.method == 'POST':
        form = edit_profile_form(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_page', pk=user.id)
    else:
        form = edit_profile_form(instance=user)

    context = {
        'form': form,
        'user': user
    }
    return render(request, 'edit_profile.html', context)