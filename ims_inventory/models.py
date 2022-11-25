from django.db import models


class Purchase(models.Model):
    quantity = models.FloatField(default=0.0, blank=False, null=False)
    product = models.ForeignKey('ims_product.Product', on_delete=models.CASCADE)
    supplier = models.ForeignKey('ims_user.Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return 'product: ' + str(self.product.name) + ' from ' + str(self.supplier.name)