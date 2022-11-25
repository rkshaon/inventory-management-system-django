from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cell = models.CharField(max_length=500, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cell = models.CharField(max_length=500, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name