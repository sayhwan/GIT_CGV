from django.db import models
from movies.models import Movie
# Create your models here.

class Cinemas(models.Model):
    numbering = models.IntegerField(default=0)
    seat = models.CharField(default="(5,5)",max_length=10)

    def __str__(self):
        return str(self.numbering)+"관"
    class Meta:
        db_table='Cinemas'
        verbose_name='극장'
        verbose_name_plural='극장'
class Ticketing(models.Model):
    cinema = models.ForeignKey(Cinemas,on_delete=models.CASCADE)
    seat_all = models.JSONField(default=dict(a=1))
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='날짜')
    movie_times = models.CharField(max_length=20,verbose_name='상영 시간',default=0)
    def __str__(self):
        return str(self.date)

    class Meta:
        db_table='ticketing'
        verbose_name='예매'
        verbose_name_plural='예매'