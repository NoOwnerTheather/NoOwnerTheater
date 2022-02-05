from django.shortcuts import render, redirect

from django.contrib import auth
from .forms import *

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
