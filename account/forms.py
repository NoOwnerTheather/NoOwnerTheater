from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from theater.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import django.contrib.auth.forms as auth_forms
from django import forms





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
        fields = ['password', 'nickname','phone','email']

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = '아이디'


class PasswordResetForm(auth_forms.PasswordResetForm):
    username = auth_forms.UsernameField(label="사용자ID")  # CharField 대신 사용

    # validation 절차:
    # 1. username에 대응하는 User 인스턴스의 존재성 확인
    # 2. username에 대응하는 email과 입력받은 email이 동일한지 확인

    def clean_username(self):
        data = self.cleaned_data['username']
        if not User.objects.filter(username=data).exists():
            raise ValidationError("해당 사용자ID가 존재하지 않습니다.")

        return data

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if username and email:
            if User.objects.get(username=username).email != email:
                raise ValidationError("사용자의 이메일 주소가 일치하지 않습니다")

    def get_users(self, email=''):
        active_users = User.objects.filter(**{
            'username__iexact': self.cleaned_data["username"],
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password()
        )

class RecoveryIdForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput,)
    email = forms.EmailField(widget=forms.EmailInput,)

    class Meta:
        model = User
        fields = ['phone', 'email']

    def __init__(self, *args, **kwargs):
        super(RecoveryIdForm, self).__init__(*args, **kwargs)
        self.fields['phone'].label = '핸드폰번호'
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control input-lg input-style',
            'id': 'form_phone',
            'placeholder':"000-0000-0000"
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control input-lg input-style',
            'id': 'form_email',
            'placeholder':"EMAIL"
        })


        