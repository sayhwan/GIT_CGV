from django.shortcuts import render,get_object_or_404
from django.views.generic import *
from movies.models import Movie
from .models import Area,Theater
# Create your views here.
class Index(ListView):
    template_name = 'ticketing/index.html'
    model = Movie

    def get_context_data(self, **kwargs):
        login_session = self.request.session.get('login_session', '')
        context = super().get_context_data(**kwargs)
        context['login_session'] = login_session
        return context

def Theaterdetail(request, t_id ):
    context = {}
    login_session = request.session.get('login_session', '')
    context['login_session'] = login_session
    area = get_object_or_404(Area,pk=t_id)
    theaters=area.theater_set.all
    context['area']=area
    context['theaters']=theaters
    return render(request, template_name='ticketing_detail', context=context)


def Areas(request, m_id ):
    movie=get_object_or_404(Movie,pk=m_id)
    context={}
    context['movie']=movie
    ticketing_list=movie.ticketing_set.all()
    theater_list=[]
    for ticketing in ticketing_list:
        theater_list.append(ticketing.theater)
    areas=[]
    for theater in theater_list:
        areas.append(theater.area)
    areas.sort(key=lambda x:x.name )
    areas=set(areas)
    context['areas']=areas
    login_session = request.session.get('login_session', '')
    context['login_session'] = login_session

    return render(request,template_name='ticketing/area.html', context=context)
def Theaters(request, m_id, a_id ):
    movie=get_object_or_404(Movie,pk=m_id)
    context={}
    context['movie']=movie
    area=get_object_or_404(Area,pk=a_id)
    context['area']=area
    ticketing_list = movie.ticketing_set.all()
    theater_list=[]
    for ticketing in ticketing_list:
        if ticketing.theater.area.name==area.name:
            theater_list.append(ticketing.theater)
    theater_list=set(theater_list)
    context['theater_list']=theater_list
    login_session = request.session.get('login_session', '')
    context['login_session'] = login_session

    return render(request,template_name='ticketing/theater.html', context=context)
def Date(request, m_id, th_id ):
    movie=get_object_or_404(Movie,pk=m_id)
    context={'movie':movie}
    theater=get_object_or_404(Theater,pk=th_id)
    context['movie_list'] = Movie.objects.all()
    context['theater']=theater
    context['area']=theater.area
    ticketing_list=list(filter(lambda x: x.movie == movie and x.theater == theater, movie.ticketing_set.all()))
    context['ticketing_list']=ticketing_list
    login_session = request.session.get('login_session', '')
    context['login_session'] = login_session

    return render(request,template_name='ticketing/date_detail.html',context=context)
