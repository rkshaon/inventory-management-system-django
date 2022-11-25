from django.shortcuts import render, redirect


def purchase_list(request):
    context = {}

    return render(request, 'purchase_list.html', context)


def purchase_add(request):
    context = {}
    return render(request, 'purchase_add.html', context)