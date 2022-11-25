from django.shortcuts import render, redirect

from ims_inventory.models import Purchase

from ims_inventory.forms import NewPurchaseForm


def purchase_list(request):
    context = {}

    return render(request, 'purchase_list.html', context)


def purchase_add(request):
    form = NewPurchaseForm()

    context = {
        'form': form,
    }

    return render(request, 'purchase_add.html', context)