from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from ims_user.models import Supplier
from ims_user.models import Customer

from ims_user.forms import NewSupplierForm
from ims_user.forms import NewCustomerForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Successfully logged in, congrats!')
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}

    return render(request, 'login.html', context)


@login_required(login_url='login')
def supplier_list(request):
    suppliers = Supplier.objects.all()

    context = {
        'suppliers': suppliers,
    }

    return render(request, 'supplier_list.html', context)


@login_required(login_url='login')
def supplier_add(request):
    if request.method == 'POST':
        form = NewSupplierForm(request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            address = request.POST.get('address')
            email = request.POST.get('email')
            cell = request.POST.get('cell')

            s, created = Supplier.objects.get_or_create(
                name=name, address=address, email=email, cell=cell)
            
            messages.info(request, 'Supplier added successfully!')
            
            return redirect('supplier_list')

    form = NewSupplierForm()

    context = {
        'form': form,
    }

    return render(request, 'supplier_add.html', context)


@login_required(login_url='login')
def customer_list(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers,
    }

    return render(request, 'customer_list.html', context)


@login_required(login_url='login')
def customer_add(request):
    if request.method == 'POST':
        form = NewSupplierForm(request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            address = request.POST.get('address')
            email = request.POST.get('email')
            cell = request.POST.get('cell')

            c, created = Customer.objects.get_or_create(
                name=name, address=address, email=email, cell=cell)
            
            messages.info(request, 'Customer added successfully!')
            
            return redirect('customer_list')

    form = NewCustomerForm()

    context = {
        'form': form
    }

    return render(request, 'customer_add.html', context)