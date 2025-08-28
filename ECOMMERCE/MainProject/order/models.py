from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import User
from inventory.models import Product
from accounts.models import Address
class Order(models.Model):
    uuid = models.UUIDField()
    payment_id = models.CharField(max_length=100,default=0)
    # order_no=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    order_amount=models.IntegerField(null=True)
    address = models.ForeignKey(Address,on_delete=models.DO_NOTHING)
   