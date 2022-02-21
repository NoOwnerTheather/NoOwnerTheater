from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import auth
from .forms import *

from django.contrib.auth import get_user_model


from django.contrib import auth
from django.contrib.auth import login, authenticate
from theater.models import User
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

from django.urls import reverse_lazy
from account.forms import PasswordResetForm
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, SetPasswordForm,
)
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import resolve_url
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views import generic, View

from django.template import RequestContext
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

from django.contrib.auth.tokens import default_token_generator
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt


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


class UserPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html' #템플릿을 변경하려면 이와같은 형식으로 입력
    success_url = reverse_lazy('account:password_reset_done')
    form_class = PasswordResetForm
    
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'account/password_reset_done_fail.html')
            
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html' #템플릿을 변경하려면 이와같은 형식으로 입력




UserModel = get_user_model()
INTERNAL_RESET_URL_TOKEN = 'set-password'
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url=reverse_lazy('account:password_reset_complete')
    template_name = 'account/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = resolve_url(settings.LOGIN_URL)
        return context


from .forms import RecoveryIdForm
from django.views.generic import View

def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "접속중인 사용자입니다.")
            return redirect('/account/main/')
        return function(request, *args, **kwargs)
    return wrap


@method_decorator(logout_message_required, name='dispatch')
class RecoveryIdView(View):
    template_name = 'account/recovery_id.html'
    recovery_id = RecoveryIdForm
    # print("phone")
    # print("phone2")

    def get(self, request):
        if request.method=='GET':
            form_id = self.recovery_id(None)
        return render(request, self.template_name, { 'form_id':form_id, })



import json
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def ajax_find_id_view(request):
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    result_id = User.objects.get(phone=phone, email=email)
    print("phone")
    print(phone)
       
    return HttpResponse(json.dumps({"result_id": result_id.username}, cls=DjangoJSONEncoder), content_type = "application/json")
