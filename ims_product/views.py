from django.shortcuts import render


def category_list(request):
    context = {}

    return render(request, 'category_list.html', context)


def product_list(request):
    context = {}

    return render(request, 'product_list.html', context)