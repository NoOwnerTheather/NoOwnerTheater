from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy


app_name = 'account'

urlpatterns = [
   path('signup/', views.signup_view, name = 'signup'),
   path('login/', views.login_view, name= 'login'),
   path("logout/", views.logout, name="logout"),
   path('user_delete/', views.user_delete, name='user_delete'),
   path('<int:pk>/', views.mypage, name = 'mypage'),
   path('user_fix/', views.user_fix, name = 'user_fix'),
   path('change_password/', views.change_password, name='change_password'),
   
   
   path('password_reset/', views.UserPasswordResetView.as_view(
      email_template_name='account/password_reset_email.html',
   ), name="password_reset"),
   path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
   path('password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(
      success_url = reverse_lazy('account:password_reset_complete')
   ), name="password_reset_confirm"),
   path('password_reset_complete/', views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete"),
   


   
   
]