from django.shortcuts import render

from ims_product.models import Category
from ims_product.models import Product


def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'category_list.html', context)


def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'product_list.html', context)