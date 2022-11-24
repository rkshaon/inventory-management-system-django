from django.urls import path

from ims_product import views

urlpatterns = [
    path('category', views.category_list, name='category_list'),
]