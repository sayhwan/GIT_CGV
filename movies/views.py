from django.shortcuts import render
from django.db.models import Count
from django.views.generic import *
from movies.models import *

# Create your views here.
class MovieList(ListView):
    model = Movie

    def get_context_data(self, **kwargs):
        login_session = self.request.session.get('login_session', '')
        context = super().get_context_data(**kwargs)
        context['login_session'] = login_session
        return context


