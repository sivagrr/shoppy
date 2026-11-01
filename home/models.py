from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name
