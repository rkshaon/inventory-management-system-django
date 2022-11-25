from django.db import models


class Inventory(models.Model):
    product = models.ForeignKey('ims_product.Product', on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0, blank=False, null=False)

    def __str__(self):
        return 'product: ' + str(self.product.name) + ' quantity: ' + str(self.quantity)


class Purchase(models.Model):
    quantity = models.FloatField(default=0.0, blank=False, null=False)
    product = models.ForeignKey('ims_product.Product', on_delete=models.CASCADE)
    supplier = models.ForeignKey('ims_user.Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return 'product: ' + str(self.product.name) + ' from ' + str(self.supplier.name)


class Sale(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0, blank=False, null=False)

    def __str__(self):
        return 'product: ' + str(self.inventory.product.name) + ' quantity: ' + str(self.quantity)