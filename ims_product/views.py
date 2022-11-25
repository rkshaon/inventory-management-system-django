from django.shortcuts import render, redirect

from ims_product.models import Category
from ims_product.models import Product

from ims_product.forms import NewCategoryForm
from ims_product.forms import NewProductForm


def category_list(request):
    categories = Category.objects.filter(is_deleted=False).order_by('name')

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
            
            category = Category.objects.create(name=name, image=image)
        
            return redirect('category_list')

    form = NewCategoryForm()
    
    context = {
        'form': form,
    }

    return render(request, 'category_add.html', context)


def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.is_deleted = True

    category.save()

    return redirect('category_list')


def product_list(request):
    products = Product.objects.filter(is_deleted=False).order_by('category__name')

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
            
            product = Product.objects.create(name=name, image=image, category=category)

            return redirect('product_list')

    form = NewProductForm()
    
    context = {
        'form': form,
    }

    return render(request, 'product_add.html', context)


def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.is_deleted = True
    product.save()

    return redirect('product_list')