from django.db import models
from datetime import date

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    age = models.IntegerField(default=0)
    age_url = models.CharField(max_length=2000,default='/')
    summary = models.TextField(max_length=2000)
    date = models.DateField(default=date.today)
    rank = models.IntegerField(default=0)
    times = models.CharField(default='120',max_length=20,verbose_name='상영시간')
    director = models.ManyToManyField('Director')
    def __str__(self):
        return self.title

    class Meta:
        db_table='movie'
        verbose_name='영화'
        verbose_name_plural='영화'

class Director(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='감독'
        verbose_name_plural='감독'