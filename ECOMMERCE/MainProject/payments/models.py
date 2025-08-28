from django.db import models
from django.contrib.auth.models  import AbstractUser
from order.models import Order
PAYMENT_CHOICES=[
    ('upi_id','upi_id'),
    ('upi_app','upi_app'),
    ('bank','bank')
]
STATUS_CHOICES=[
    ('C','COMPLETED'),
    ('N','NOTCOMPLETED')
]
class payment(models.Model):
    payment_id=models.IntegerField()
    method=models.CharField(max_length=10,choices=PAYMENT_CHOICES)
    amount=models.IntegerField()
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    status =models.CharField(max_length=1,choices=STATUS_CHOICES)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

