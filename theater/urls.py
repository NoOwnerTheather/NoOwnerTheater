from django.urls import path
from . import views

app_name = 'theater'

urlpatterns = [
   path('', views.main, name='main'),
   path('business_list/', views.business_list, name="business_list"),
   path('<int:pk>/business/', views.business_detail, name="business_detail"),
   path('business_search/', views.business_search, name="business_search"),
]