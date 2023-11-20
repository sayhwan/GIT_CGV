from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    age = models.IntegerField(max_)