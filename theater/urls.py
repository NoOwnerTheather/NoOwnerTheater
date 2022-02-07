from django.urls import path
from . import views

app_name = 'theater'

urlpatterns = [
   path('', views.main, name='main'),
   path('movie_enroll/',views.movie_enroll,name='enroll'),
]