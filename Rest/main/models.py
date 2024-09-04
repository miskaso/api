from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=55)
    info = models.TextField()
    country = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.author}"


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.name.username
