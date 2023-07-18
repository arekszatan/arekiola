from django.db import models


class WalletListDb(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    female = models.BooleanField(default=False, blank=True)
    person = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.person
