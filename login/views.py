from django.shortcuts import render, redirect
from .models import User
from django.db import transaction
from argon2 import PasswordHasher
from .forms import RegisterForm, LoginForm


# 웹 페이지에서 받은 정보 DB로 받아오기
def Register(request):
    register_form = RegisterForm()
    context = {'forms': register_form}
    if request.method == 'GET':
        return render(request, 'login/register.html', context)

    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User(
                user_id=register_form.user_id,
                user_pw=register_form.user_pw,
                user_name=register_form.user_name,
                user_email=register_form.user_email,
            )
            user.save()
            return redirect('/')
        # ERROR 출력
        else:
            context['forms'] = register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'login/register.html', context)


# 로그인 함수 정의
def Login(request):
    # form에서 만들었던 LoginForm
    loginform = LoginForm()
    context = {'forms': loginform}

    if request.method == 'GET':
        return render(request, 'login/login.html', context)

    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session'] = loginform.login_session
            request.session.set_expiry(0)
            return redirect('/')
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'login/login.html', context)


# 로그아웃 정의
def Logout(request):
    request.session.flush()
    return redirect('/')