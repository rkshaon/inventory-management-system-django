from django.urls import path

from ims_inventory import views


urlpatterns = [
    path('purchase', views.purchase_list, name='purchase_list'),
    path('purchase/add', views.purchase_add, name='purchase_add'),
    path('sale', views.sale_list, name='sale_list'),
    # path('sale/add', views.sale_add, name='sale_add'),
]