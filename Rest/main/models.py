from django.db import models


# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=55)
    info = models.TextField()
    country = models.CharField(max_length=55)

    def __str__(self):
        return self.name
