from django.db import models


class ShoppingOtherDb(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=180)
    done = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.product
