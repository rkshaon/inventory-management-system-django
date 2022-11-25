from django.shortcuts import render, redirect

from ims_product.models import Category
from ims_product.models import Product

from ims_product.forms import NewCategoryForm
from ims_product.forms import NewProductForm


def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'category_list.html', context)


def category_add(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST, request.FILES)

        if form.is_valid():
            image = request.FILES.get('image')
            name = request.POST.get('name')
            
            c, created = Category.objects.get_or_create(name=name, image=image)
        
            return redirect('category_list')

    form = NewCategoryForm()
    
    context = {
        'form': form,
    }

    return render(request, 'category_add.html', context)


def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'product_list.html', context)


def product_add(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            name = request.POST.get('name')
            image = request.FILES.get('image')
            category = Category.objects.get(id=request.POST.get('category'))
            
            p, created = Product.objects.get_or_create(name=name, image=image, category=category)

            return redirect('product_list')

    form = NewProductForm()
    
    context = {
        'form': form,
    }

    return render(request, 'product_add.html', context)