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
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models as m
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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
        auth.login(request, user,  backend='django.contrib.auth.backends.ModelBackend')
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
      auth.login(request, user,  backend='django.contrib.auth.backends.ModelBackend')
      return redirect('theater:main')

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

def mypage(request,pk):
  user = get_object_or_404(User, pk=pk)

  #counting=Movie.objects.count()

  #counted=User.movie_set.count()
  #print(counted)
  #MyUser.follower.all()

  #print(counting)
  
  ctx={
    'user':user, #'counitng':counting
  }
  return render(request, 'account/mypage.html',context=ctx)

@require_POST
@login_required
def user_delete(request):
    request.user.delete()
    return redirect('theater:main')


@login_required
def user_fix(request):
  post=get_object_or_404(User,id=request.user.id)
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect('account:mypage',request.user.id)
    
  else:
    form = CustomUserChangeForm(instance =post)
    ctx={'form':form}
    return render(request, 'account/user_fix.html', context=ctx)

@login_required
def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)

        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user) #비밀번호 수정해도 로그아웃되지않게
            return redirect('account:mypage', request.user.id)
    
    else:
        password_change_form = PasswordChangeForm(request.user)
        ctx = {'form':password_change_form}
    return render(request, 'account/change_password.html', context=ctx)

class AuthSMS(APIView):
   def post(self, request):
      try:
         p_num = request.data['phone_number']
      except KeyError:
         return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
      else:
         m.AuthSMS.objects.update_or_create(phone_number=p_num)
         return Response({'message': 'OK'})

   def get(self, request):
      try:
         p_num = request.query_params['phone_number']
         a_num = request.query_params['auth_number']
      except KeyError:
         return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
      else:
         result = m.AuthSMS.check_auth_number(p_num, a_num)
         return Response({'message': 'OK', 'result': result})


