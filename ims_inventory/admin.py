from django.contrib import admin

from ims_inventory.models import Inventory
from ims_inventory.models import Purchase
# from ims_inventory.models import Sale

admin.site.register(Inventory)
admin.site.register(Purchase)
# admin.site.register(Sale)