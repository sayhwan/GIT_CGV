from django.urls import path
from login.views import *

urlpatterns = [
    path('Login/', Login, name='login'),
    path('Register/', Register, name='register'),
    path('Logout/', Logout, name='logout'),
    path('mypage/', Mypage, name='mypage'),
]
app_name='login'