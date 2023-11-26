from django.urls import path
from ticketing.views import *

app_name = 'ticketing'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('area/<int:m_id>/', Areas, name='area'),
    path('theater/<int:m_id>/<int:a_id>/', Theaters, name='theater'),
    path('date/<int:m_id>/<int:th_id>/', Date, name='date'),

]