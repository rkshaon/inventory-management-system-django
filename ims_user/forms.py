from django import forms

from ims_user.models import Supplier
from ims_user.models import Customer


class NewSupplierForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter supplier name',
    }), required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter full address',
        'rows': '3',
    }), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter e-mail address',
    }), required=False)
    cell = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter cell number',
    }), required=False)

    class Meta:
        model = Supplier
        fields = {'name', 'address', 'email', 'cell'}


class NewCustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter supplier name',
    }), required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter full address',
        'rows': '3',
    }), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter e-mail address',
    }), required=False)
    cell = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter cell number',
    }), required=False)

    class Meta:
        model = Customer
        fields = {'name', 'address', 'email', 'cell'}
