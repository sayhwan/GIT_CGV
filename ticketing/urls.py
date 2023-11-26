from django.urls import path
from ticketing.views import *

app_name = 'ticketing'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('area/<int:m_id>/', Areas, name='area'),
    path('theater/<int:m_id>/<int:a_id>/', Theaters, name='theater'),
    path('date/<int:m_id>/<int:th_id>/', Date, name='date'),
    path('seat/<int:t_id>/', Seat,name='seat'),
    path('ticketing/<int:t_id>', Ticketing_seat, name='ticketing'),
    path('seat/<int:t_id>/button/',Button, name='button'),
]