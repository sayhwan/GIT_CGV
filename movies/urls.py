from django.urls import path
from movies.views import *

app_name = 'movies'
urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]

