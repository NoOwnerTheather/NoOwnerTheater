from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
   path('signup/', views.signup_view, name = 'signup'),
   path('login/', views.login_view, name= 'login'),
   path("logout/", views.logout, name="logout"),
   path('user_delete/', views.user_delete, name='user_delete'),
   path('<int:pk>/', views.mypage, name = 'mypage'),
   path('user_fix/', views.user_fix, name = 'user_fix'),
   path('change_password/', views.change_password, name='change_password'),
   # path('check_check/',views.AuthSMS,name='check_check')
]