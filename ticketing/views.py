from django.shortcuts import render,get_object_or_404,reverse
from django.views.generic import *
from movies.models import Movie
from .models import Area,Theater,Ticketing
from login.models import *
from login.decorators import login_required
from django.http import HttpResponseRedirect
import json
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
    request.session['button']=0
    return render(request,template_name='ticketing/date_detail.html',context=context)
@login_required
def Seat(request, t_id):
    login_session = request.session.get('login_session', '')
    button = request.session.get('button','')
    ticketing = get_object_or_404(Ticketing, pk=t_id)
    print(login_session)
    if login_session in ticketing.user:
        return HttpResponseRedirect(reverse(viewname='base'))
    user=get_object_or_404(User, user_id=login_session)
    seat_list = ticketing.seat_all.copy()
    rows = len(seat_list)
    columns = len(seat_list[0])
    context = {}
    context['user']=user
    context['ticketing']=ticketing
    context['login_session']=login_session
    context['row']="1fr "*rows
    context['column']="1fr "*columns
    context['seat_list']=seat_list
    context['error']=button
    return render(request, template_name='ticketing/seat.html', context=context)

def Ticketing_seat(request,t_id):
    login_session = request.session.get('login_session', '')
    ticketing = get_object_or_404(Ticketing, pk=t_id)
    user = get_object_or_404(User, user_id=login_session)
    button=request.session.get('button','')
    if request.method=='POST':
        a=[]
        if button==True:
            return HttpResponseRedirect(reverse('ticketing:seat', args=(t_id,)))
        for i in range(len(ticketing.seat_all)):
            for j in range(len(ticketing.seat_all[0])):
                if ticketing.seat_all[i][j]==2:
                    ticketing.seat_all[i][j]=1
                    a.append((i,j))
        user_ticket = User_ticket()
        user_ticket.theater = ticketing.theater
        user_ticket.movie = ticketing.movie
        user_ticket.date = ticketing.date
        user_ticket.seat = a
        user_ticket.cinema = ticketing.cinema
        user_ticket.save()
        user.user_ticket.add(user_ticket)
        user.save()
        ticketing.user.append(user.user_id)
        ticketing.save()

        return HttpResponseRedirect(reverse(viewname='base'))



def Button(request,t_id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        ticketing = get_object_or_404(Ticketing,pk=t_id)
        ticketing.seat_all[data['row']][data['column']]=data['value']
        ticketing.save()
        li=ticketing.seat_all.copy()
        flag=0
        while flag == 0:
            for row in li:
                for column in row:
                    if column == 2:
                        flag=1
            break
        request.session['button']=not bool(flag)
        return HttpResponseRedirect(reverse('ticketing:seat', args=(t_id,)))
    return HttpResponseRedirect(reverse('ticketing:seat', args=(t_id,)))