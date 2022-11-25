from django.shortcuts import render, redirect

from ims_user.models import Supplier

from ims_user.forms import NewSupplierForm


def supplier_list(request):
    suppliers = Supplier.objects.all()

    context = {
        'suppliers': suppliers,
    }

    return render(request, 'supplier_list.html', context)


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
            
            return redirect('supplier_list')

    form = NewSupplierForm()

    context = {
        'form': form,
    }

    return render(request, 'supplier_add.html', context)