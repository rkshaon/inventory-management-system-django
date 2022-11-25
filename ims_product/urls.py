from django.urls import path

from ims_product import views

urlpatterns = [
    path('category', views.category_list, name='category_list'),
    path('category/add', views.category_add, name='category_add'),
    path('category/delete/<pk>', views.category_delete, name='category_delete'),
    path('', views.product_list, name='product_list'),
    path('add', views.product_add, name='product_add'),
    path('delete/<pk>', views.product_delete, name='product_delete'),
]