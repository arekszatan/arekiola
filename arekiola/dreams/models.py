from django.db import models


class Post(models.Model):
    objects = None
    document = models.FileField(upload_to='img/%Y%m%d/',
                                null=True, blank=True)

