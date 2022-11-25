from django import forms

from ims_product.models import Product
from ims_user.models import Supplier
from ims_user.models import Customer
from ims_inventory.models import Purchase
from ims_inventory.models import Inventory
from ims_inventory.models import Sale


class NewPurchaseForm(forms.ModelForm):
    quantity = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter quantity of the product',
    }), required=True)
    product = forms.ModelChoiceField(queryset=Product.objects.filter(is_deleted=False), widget=forms.Select(attrs={
        'class': 'form-control',
    }), required=True)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), required=True)
    
    class Meta:
        model = Purchase
        fields = {'quantity', 'product'}


class NewSaleForm(forms.ModelForm):
    quantity = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter quantity of the product',
    }), required=True)
    inventory = forms.ModelChoiceField(queryset=Inventory.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), required=True)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), required=True)

    class Meta:
        model = Sale
        fields = {'quantity', 'inventory', 'customer'}