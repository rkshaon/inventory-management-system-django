from django.shortcuts import render

from ims_product.models import Category


def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'category_list.html', context)


def product_list(request):
    context = {}

    return render(request, 'product_list.html', context)