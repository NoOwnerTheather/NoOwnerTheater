from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
 

app_name = 'theater'

urlpatterns = [
   path('', views.main, name='main'),
   path('movie_enroll/',views.movie_enroll,name='enroll'),
   path('<int:pk>/movie_fix/',views.movie_fix,name='movie_fix'),
   path('<int:pk>/movie_delete/',views.movie_delete,name='movie_delete'),
   path('<int:pk>/review_enroll/',views.review_enroll,name='review_enroll'),
   path('<int:pk>/<int:gk>/review_fix/',views.review_fix,name='review_fix'),
   path('<int:pk>/<int:gk>/review_delete/',views.review_delete,name='review_delete'),
   path('info_enroll/',views.info_enroll,name="info_enroll"),
   path('<int:pk>/info_fix/',views.info_fix,name='info_fix'),
   path('<int:pk>/info_delete/',views.info_delete,name='info_delete'),
   path('preview/',views.preview,name="preview"), #시사회 페이지
   path('preview/<int:pk>/',views.preview_detail,name='preview_detail'), #시사회 디테일페이지
   
   path('preview/<int:pk>/like_ajax/', views.like_ajax, name='like_ajax'),

   path("preview/<int:pk>/write_comment/", views.write_comment, name='write_comment'),
   path("preview/<int:pk>/del_comment/", views.del_comment, name='del_comment'),
   path('ckeditor_upload/', include('ckeditor_uploader.urls')),
   path('ckeditor/', include('ckeditor_uploader.urls')),
   path('business_list/', views.business_list, name="business_list"),
   path('<int:pk>/business/', views.business_detail, name="business_detail"),
   path('business_search/', views.business_search, name="business_search"),
   path('chart_list/', views.chart_list, name="chart_list"),
   path('movie_search/', views.movie_search, name="movie_search"),
   path('movie_list_popular/', views.movie_list_popular, name="movie_list_popular"),
   path('movie_list_recent/', views.movie_list_recent, name="movie_list_recent"),
   path('genre_order/', views.genre_order, name="genre_order"),


   path('business_hits_ajax/',views.business_hits_ajax, name='business_hits_ajax'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
