from django.shortcuts import render
from login.models import *

def Base(request):
    context = {}
    # 로그인 세션 정의
    login_session = request.session.get('login_session', '')

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    return render(request, 'base.html', context)