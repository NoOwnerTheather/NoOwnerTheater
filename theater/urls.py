from django.urls import path
from . import views

app_name = 'theater'

urlpatterns = [
   path('', views.main, name='main'),
   path('movie_enroll/',views.movie_enroll,name='enroll'),
   path('<int:pk>/movie_fix/',views.movie_fix,name='movie_fix'),
   path('<int:pk>/movie_delete/',views.movie_delete,name='movie_delete'),
   path('review_enroll/',views.review_enroll,name='review_enroll'),
   path('<int:pk>/review_fix/',views.review_fix,name='review_fix'),
   path('<int:pk>/review_delete/',views.review_delete,name='review_delete'),
   path('info_enroll',views.info_enroll,name="info_enroll"),
   path('<int:pk>/info_fix/',views.info_fix,name='info_fix'),
   path('<int:pk>/info_delete/',views.info_delete,name='info_delete')
]