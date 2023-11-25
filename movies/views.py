from django.shortcuts import render
from django.db.models import Count
from django.views.generic import *
from movies.models import *

# Create your views here.
class MovieList(ListView):
    model = Movie

class MovieDetail(DetailView):
    model = Movie
