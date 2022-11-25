from django.shortcuts import render

from ims_user.models import Supplier


def supplier_list(request):
    suppliers = Supplier.objects.all()

    context = {
        'suppliers': suppliers,
    }

    return render(request, 'supplier_list.html', context)


def supplier_add(request):
    context = {}

    return render(request, 'supplier_add.html', context)