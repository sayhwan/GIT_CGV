from django.shortcuts import render,get_object_or_404
from django.views.generic import *
from movies.models import Movie
from .models import Ticketing,Cinemas
import json
# Create your views here.

class Index(TemplateView):
    template_name = 'ticketing/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_list']=Movie.objects.all()
        context['ticketing_list']=Ticketing.objects.all()
        return context
def Date(request, m_id):
    movie=get_object_or_404(Movie,pk=m_id)
    context={'movie':movie}
    context['movie_list'] = Movie.objects.all()
    context['ticketing_list'] = Ticketing.objects.all()

    return render(request,template_name='ticketing/date_detail.html',context=context)