from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='category', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    