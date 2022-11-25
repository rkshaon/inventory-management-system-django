from django import forms
from django.forms import ClearableFileInput

from ims_product.models import Category
from ims_product.models import Product


class NewCategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter category name',
        }), required=True)
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Category
        fields = {'name', 'image'}


class NewProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        'class': 'form-control',
        'placeholder': 'Enter product name',
    ), required=True)
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)
    # category = forms.
    # image = models.ImageField(upload_to='product', null=True, blank=True)
    # category

    class Meta:
        model = Product
        fields = {}