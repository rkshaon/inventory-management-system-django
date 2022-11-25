from django.contrib import admin

from ims_inventory.models import Inventory
from ims_inventory.models import Purchase

admin.site.register(Inventory)
admin.site.register(Purchase)