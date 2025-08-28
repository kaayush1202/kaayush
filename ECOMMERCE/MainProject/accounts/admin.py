from django.contrib import admin

# Register your models here.
from .models import User
# from inventory.models import Product
admin.site.register(User)
# admin.site.register([Product])

