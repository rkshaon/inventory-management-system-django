from django.urls import path

from ims_home import views

urlpatterns = [
    path('', views.index, name='index')
]