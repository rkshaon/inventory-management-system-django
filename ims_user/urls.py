from django.urls import path

from ims_user import views


urlpatterns = [
    path('supplier', views.supplier_list, name='supplier_list'),
    path('suppler/add', views.supplier_add, name='supplier_add'),
    path('customer', views.customer_list, name='customer_list'),
]