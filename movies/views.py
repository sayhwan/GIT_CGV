from django.shortcuts import render
from django.db.models import Count
from django.views.generic import *
from movies.models import *

# Create your views here.
class MovieList(ListView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset1 = Movie.objects.all()
        context['rows']="1fr "*(queryset1.count()//4)
        return context


