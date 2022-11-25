from django import forms

from ims_product.models import Product
from ims_user.models import Supplier
from ims_inventory.models import Purchase


class NewPurchaseForm(forms.ModelForm):
    quantity = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter quantity of the product',
    }), required=True)
    # product = forms.ChoiceField(widget=forms.Select(attrs={
        
    # }), required=True)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), required=True)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), required=True)

    # category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
    #     'class': 'form-control',
    # }), required=True)

    class Meta:
        model = Purchase
        fields = {'quantity', 'product'}