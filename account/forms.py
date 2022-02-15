from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from theater.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2', 'nickname', 'phone','type','gender','email','age']
    labels={
            'username':'아이디',
    }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username','password', 'nickname','phone','email']

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = '아이디'
        