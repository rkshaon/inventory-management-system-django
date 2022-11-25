from django.contrib import admin

from ims_user.models import Supplier
from ims_user.models import Customer

admin.site.register(Supplier)
admin.site.register(Customer)