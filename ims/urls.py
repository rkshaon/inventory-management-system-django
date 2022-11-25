"""ims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ims_inventory import views as inventory_view
from ims_user import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inventory_view.index, name='index'),
    path('login', user_view.user_login, name='login'),
    path('product/', include('ims_product.urls')),
    path('inventory/', include('ims_inventory.urls')),
    path('user/', include('ims_user.urls')),
]
