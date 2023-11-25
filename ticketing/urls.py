from django.urls import path
from ticketing.views import *

app_name = 'ticketing'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:m_id>/', Date, name='date'),
]