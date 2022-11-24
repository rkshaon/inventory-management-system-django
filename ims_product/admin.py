from django.contrib import admin

from ims_product.models import Category
from ims_product.models import Product


admin.site.register(Category)
admin.site.register(Product)