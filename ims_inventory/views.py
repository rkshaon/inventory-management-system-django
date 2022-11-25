from django.shortcuts import render, redirect

from ims_product.models import Product
from ims_user.models import Supplier
from ims_inventory.models import Inventory
from ims_inventory.models import Purchase

from ims_inventory.forms import NewPurchaseForm
from ims_inventory.forms import NewSaleForm


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
    purchases = Purchase.objects.all()

    context = {
        'purchases': purchases,
    }

    return render(request, 'sale_list.html', context)


def sale_add(request):
    form = NewSaleForm()

    context = {
        'form': form,
    }

    return render(request, 'sale_add.html', context)