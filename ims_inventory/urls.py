from django.urls import path

from ims_inventory import views


urlpatterns = [
    path('purchase', views.purchase_list, name='purchase_list'),
]