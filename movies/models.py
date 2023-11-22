from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    age = models.IntegerField(default=0)
    summary = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default=0)
    def __str__(self):
        return self.title

    class Meta:
        db_table='movie'
        verbose_name='영화'
        verbose_name_plural='영화'
