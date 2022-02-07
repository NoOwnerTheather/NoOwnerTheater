from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import auth
from .forms import *

from django.contrib.auth import get_user_model



from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from random import *

def login_user(request): # 로그인 중인 Profile object
    return User.objects.get(user=request.user)





def login_view(request):
  if request.method == 'POST':
    form = CustomAuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = auth.authenticate(
        request=request,
        username=username,
        password=password
      )

      if user is not None:
        auth.login(request, user)
        return redirect('theater:main')

    
  else:
    form = CustomAuthenticationForm()
  
  context = {
        'form': form,
  } 
  return render(request, 'account/login.html', context)


def logout(request):
   auth.logout(request)
   return redirect('theater:main')


def signup_view(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth.login(request, user)
      return redirect('theater:main')
    return redirect('account:signup')

  else:
    form = SignupForm()
  
  context = {
        'form': form,
  } 
  return render(request, 'account/signup.html', context)

'''
def detail(request,pk):
  User=get_user_model()
  user=get_object_or_404(User, pk=pk)
  ctx={
    'user':user
  }
  return render(request, 'account/detail.html',context=ctx)
  '''

def detail(request,pk):
  user = get_object_or_404(User, pk=pk)
  ctx={
    'user':user
  }
  return render(request, 'account/detail.html',context=ctx)
