from django.db import models
from django.contrib.auth.models import AbstractUser
from inventory.models import Product
from order.models import Order
class OrderDetail(models.Model):
        product=models.ForeignKey(Product,on_delete=models.CASCADE)
        order=models.ForeignKey(Order,on_delete=models.CASCADE)
        quantity=models.IntegerField()
        price=models.DecimalField(max_digits=10,decimal_places=2)