from django.db import models
from django.contrib.auth.models import AbstractUser

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class Brand(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, blank=True, null=True, help_text="Country of origin")
    founded_date = models.DateField(blank=True, null=True, help_text="Date brand was founded")
    logo = models.ImageField(upload_to="media/images/brand/")
    tagline = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True,help_text="Category name")
    slug = models.SlugField(max_length=120, unique=True,  help_text="URL-friendly identifier")
    description = models.TextField(blank=True, null=True,help_text="Optional category description")
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='children',help_text="Optional parent category for hierarchy")
    def __str__(self):
        names = [self.name]
        current = self.parent
        while current is not None:
            names.append(current.name)
            current = current.parent
        return " -> ".join(reversed(names))

class Product(TimestampedModel):
    image=models.ImageField(upload_to='images/product/')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,through="ProductCategory")
    product_name=models.CharField(max_length=20,blank=None)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    def __str__(self):
        return self.brand.__str__() + " "+str(self.item )+ " of ₹"+str(self.price)
class ProductCategory(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
