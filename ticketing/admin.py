from django.contrib import admin
# Register your models here.

from django.contrib import admin
from .models import Ticketing,Cinemas,Area,Theater
@admin.register(Ticketing)
class TicketingAdmin(admin.ModelAdmin):
    list_display = ('cinema', 'movie','date','theater','user')
    fields=['cinema','movie','date','theater']
    def save_model(self, request, obj, form, change):
        obj.movie_times = obj.movie.times
        obj.save()
        a=obj.cinema.seat
        n=int(a[1:a.index(',')])
        m=int(a[a.index(',')+1:-1])
        obj.seat_all=[[0 for x in range(n)]for y in range(m)]
        obj.user=[]
        obj.save()



@admin.register(Cinemas)
class CinemasAdmin(admin.ModelAdmin):
    pass
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass
@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):

    list_display = ('name', 'area')
    fields = ['name', 'area']
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.area.theaters+=1
        obj.area.save()