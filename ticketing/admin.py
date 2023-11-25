from django.contrib import admin
# Register your models here.

from django.contrib import admin
from .models import Movie, Ticketing,Cinemas
@admin.register(Ticketing)
class TicketingAdmin(admin.ModelAdmin):
    list_display = ('cinema', 'seat_all','movie', 'movie_times','date')

    def save_model(self, request, obj, form, change):
        # obj는 현재 수정 중인 Ticketing의 인스턴스입니다.
        # form은 TicketingAdmin에서 사용되는 폼입니다.

        # 만약 Movie의 times를 Ticketing의 movie_times로 설정하고자 한다면, 아래와 같이 할 수 있습니다.
        obj.movie_times = obj.movie.times
        obj.save()
        a=obj.cinema.seat
        n=int(a[1:a.index(',')])
        m=int(a[a.index(',')+1:-1])
        obj.seat_all=[[0 for x in range(n)]for y in range(m)]
        obj.save()



@admin.register(Cinemas)
class CinemasAdmin(admin.ModelAdmin):
    pass
