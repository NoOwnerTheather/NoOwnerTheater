from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from theater.models import User

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2', 'nickname', 'phone','type','gender','email']
    labels={
            'username':'아이디',
    }


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = '아이디'
        