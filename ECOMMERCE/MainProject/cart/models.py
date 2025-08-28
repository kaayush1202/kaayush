from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import User
from inventory.models import Product

class Cart(models.Model):
    # cart_item=models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

