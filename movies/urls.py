from django.urls import path
from movies.views import *

app_name = 'movies'
urlpatterns = [
    path('movie_list/', MovieList.as_view(), name='movie_list')
]

