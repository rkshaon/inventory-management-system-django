from django.urls import path

from ims_user import views


urlpatterns = [
    path('supplier', views.supplier_list, name='supplier_list'),
]