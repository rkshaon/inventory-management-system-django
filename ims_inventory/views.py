from django.shortcuts import render, redirect

from ims_product.models import Product
from ims_user.models import Supplier
from ims_inventory.models import Purchase

from ims_inventory.forms import NewPurchaseForm


def purchase_list(request):
    purchases = Purchase.objects.all()

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

            p, created = Purchase.objects.get_or_create(
                quantity=quantity,
                supplier=supplier,
                product=product)
            
            return redirect('purchase_list')

    form = NewPurchaseForm()

    context = {
        'form': form,
    }

    return render(request, 'purchase_add.html', context)