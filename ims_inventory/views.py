from django.shortcuts import render, redirect
from django.db.models import Sum

from ims_product.models import Category
from ims_product.models import Product
from ims_user.models import Supplier
from ims_user.models import Customer
from ims_inventory.models import Inventory
from ims_inventory.models import Purchase
from ims_inventory.models import Sale

from ims_inventory.forms import NewPurchaseForm
from ims_inventory.forms import NewSaleForm


def index(request):
    inventories = Inventory.objects.all().order_by('-quantity')
    total_inventory_products_count = Inventory.objects.all().aggregate(Sum('quantity'))
    total_categories = Category.objects.filter(is_deleted=False).count()
    total_products = Product.objects.filter(is_deleted=False).count()
    total_customers = Customer.objects.filter(is_deleted=False).count()
    total_suppliers = Supplier.objects.filter(is_deleted=False).count()

    context = {
        'inventories': inventories,
        'total_inventory_products_count': total_inventory_products_count['quantity__sum'],
        'total_categories': total_categories,
        'total_products': total_products,
        'total_customers': total_customers,
        'total_suppliers': total_suppliers,
    }
    
    return render(request, 'index.html', context)

    
def purchase_list(request):
    purchases = Purchase.objects.all().order_by('-id')

    context = {
        'purchases': purchases,
    }

    return render(request, 'purchase_list.html', context)


def purchase_add(request):
    if request.method == 'POST':
        form = NewPurchaseForm(request.POST)

        if form.is_valid():
            quantity = request.POST.get('quantity')
            supplier = Supplier.objects.get(id=request.POST.get('supplier'))
            product = Product.objects.get(id=request.POST.get('product'))

            purchase = Purchase.objects.create(
                quantity=quantity, supplier=supplier, product=product
            )

            inventory, created = Inventory.objects.get_or_create(
                product=product
            )

            inventory.quantity = inventory.quantity + float(quantity)
            inventory.save()
            
            return redirect('purchase_list')

    form = NewPurchaseForm()

    context = {
        'form': form,
    }

    return render(request, 'purchase_add.html', context)


def sale_list(request):
    sales = Sale.objects.all().order_by('-id')

    context = {
        'sales': sales,
    }

    return render(request, 'sale_list.html', context)


def sale_add(request):
    if request.method == 'POST':
        form = NewSaleForm(request.POST)

        if form.is_valid():
            customer = Customer.objects.get(id=request.POST.get('customer'))
            inventory = Inventory.objects.get(id=request.POST.get('inventory'))
            quantity = request.POST.get('quantity')

            sale = Sale.objects.create(customer=customer, inventory=inventory, quantity=quantity)

            inventory.quantity = inventory.quantity - float(quantity)
            inventory.save()

            return redirect('sale_list')

    form = NewSaleForm()

    context = {
        'form': form,
    }

    return render(request, 'sale_add.html', context)