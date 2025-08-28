from django.contrib import admin
from .models import Product,Category,Brand
# Register your models here.
admin.site.register([Product,Category,Brand])