from django.urls import path
from . import views

app_name = 'theater'

urlpatterns = [
   path('', views.main, name='main'),
   path('business_list/', views.business_list, name="business_list"),
   path('<int:pk>/business/', views.business_detail, name="business_detail"),
   path('business_search/', views.business_search, name="business_search"),
   path('chart_list/', views.chart_list, name="chart_list"),
   path('movie_search/', views.movie_search, name="movie_search"),
   path('movie_list_popular/', views.movie_list_popular, name="movie_list_popular"),
   path('movie_list_recent/', views.movie_list_recent, name="movie_list_recent"),
   path('genre_order/', views.genre_order, name="genre_order"),


]