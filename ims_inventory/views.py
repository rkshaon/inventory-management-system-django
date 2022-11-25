from django.shortcuts import render, redirect


def purchase_list(reqeust):
    context = {}

    return render(reqeust, 'purchase_list.html', context)