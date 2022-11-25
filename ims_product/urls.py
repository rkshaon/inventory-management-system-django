from django.urls import path

from ims_product import views

urlpatterns = [
    path('category', views.category_list, name='category_list'),
    path('category/add', views.category_add, name='category_add'),
    path('', views.product_list, name='product_list'),
]