from django.db import models


class ColorDb(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    textColor = models.CharField(max_length=10)

    def __str__(self):
        return self.name
