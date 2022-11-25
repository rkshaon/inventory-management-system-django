from django.shortcuts import render

from ims_user.models import Supplier


def supplier_list(request):
    suppliers = Supplier.objects.all()

    context = {
        'suppliers': suppliers,
    }
    
    return render(request, 'supplier_list.html', context)