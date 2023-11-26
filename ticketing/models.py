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
class Area(models.Model):
    AREA_CHOICES = [
        ('서울', 'Seoul'),
        ('경기', 'Gyeonggi'),
        ('인천', 'Incheon'),
        ('강원', 'Gangwon'),
        ('대전/충청', 'Daejeon/Chungcheong'),
        ('대구', 'Daegu'),
        ('부산/울산', 'Busan/Ulsan'),
        ('경상', 'Gyeongsang'),
        ('광주/전라/제주', 'Gwangju/Jeolla/Jeju'),

    ]
    name = models.CharField(max_length=100,choices=AREA_CHOICES)
    theaters = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    class Meta:
        db_table='area'
        verbose_name='지역'
        verbose_name_plural='지역'
class Theater(models.Model):
    name=models.CharField(max_length=100)
    area=models.ForeignKey(Area,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        db_table='theater'
        verbose_name='영화관'
        verbose_name_plural='영화관'

class Ticketing(models.Model):
    cinema = models.ForeignKey(Cinemas,on_delete=models.CASCADE)
    seat_all = models.JSONField(default=list)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='날짜')
    movie_times = models.CharField(max_length=20,verbose_name='상영 시간',default=0)
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.date)

    class Meta:
        db_table='ticketing'
        verbose_name='예매'
        verbose_name_plural='예매'
