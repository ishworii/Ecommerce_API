from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    url = models.URLField()
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.name
