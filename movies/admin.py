from django.contrib import admin
from movies.models import Movie,Director

admin.site.register(Director)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','age','rank','age_url')
    fields=['title','image','age','summary','date', 'rank','times', 'director']
    def save_model(self, request, obj, form, change):
        if obj.age == 0:
            obj.age_url = "../media/images/movie_all.svg"
        elif obj.age == 12:
            obj.age_url = "../media/images/movie_12.svg"
        elif obj.age == 15:
            obj.age_url = "../media/images/movie_15.svg"
        elif obj.age == 18:
            obj.age_url = "../media/images/movie_18.svg"
        else:
            obj.age_url = "../media/images/movie_reject.svg"
        obj.save()
