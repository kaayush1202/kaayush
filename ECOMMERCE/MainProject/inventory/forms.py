from django.forms import ModelForm
from .models import Product,Brand,Category
class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
class BrandCreateForm(ModelForm):
    class Meta:
        model= Brand
        fields="__all__"

class CategoryCreateForm(ModelForm):
    class Meta:
        model= Category
        fields="__all__"