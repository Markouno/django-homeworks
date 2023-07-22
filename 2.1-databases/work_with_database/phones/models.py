from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=250)
    price = models.FloatField(max_length=12)
    release_date = models.CharField(max_length=12)
    lte_exists = models.BooleanField()
    slug = models.SlugField()
