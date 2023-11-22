from django.shortcuts import render
from django.views.generic import *
from books.models import *

# Create your views here.
class MovieList(ListView):
    model = Movie

