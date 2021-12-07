
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as portal_logout

from . import forms

def login(request):
    message=''
    form=forms.LoginForm()
    if request.method == 'POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request, user)
                message=f'hello {user.username}'
                return redirect('portaljob_activity:index')
                
            else:
                message=f'Cannot logged'
                redirect('portaljob_visitor:index')
    return render(request,'registration/login.html',context={'message':message,'form':form})

def logout(request):
    portal_logout(request)
    return redirect('registration:login')