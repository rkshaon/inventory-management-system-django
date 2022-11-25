from django import forms
from django.forms import ClearableFileInput

from ims_product.models import Category


class NewCategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter category name',
        }), required=True)
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Category
        fields = {'name', 'image'}