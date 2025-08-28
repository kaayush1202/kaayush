from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER_CHOICE = [
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
]
class User(AbstractUser):
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE)
    verified = models.BooleanField(default=False)
    user_type = models.CharField(max_length=8,choices=(['Customer',"Customer"],['Supplier','Supplier']))


class Address(models.Model):
    title =  models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=40)
    address_line2 = models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="address")
    def __str__(self):
        return self.title