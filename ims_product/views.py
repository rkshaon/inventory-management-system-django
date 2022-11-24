from django.shortcuts import render

def category_list(request):
    context = {}

    return render(request, 'category_list.html', context)