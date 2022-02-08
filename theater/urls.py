from django.urls import path
from . import views

app_name = 'theater'

urlpatterns = [
   path('', views.main, name='main'),
   path('preview/',views.preview,name="preview"), #시사회 페이지
   path('preview/<int:pk>/',views.preview_detail,name='preview_detail'), #시사회 디테일페이지

   path('preview/<int:pk>/like_ajax/', views.like_ajax, name='like_ajax'),

   path("preview/<int:pk>/write_comment/", views.write_comment, name='write_comment'),
   path("preview/<int:pk>/del_comment/", views.del_comment, name='del_comment'),


   path('business_list/', views.business_list, name="business_list"),
   path('<int:pk>/business/', views.business_detail, name="business_detail"),
   path('business_search/', views.business_search, name="business_search"),
   path('business_hits_ajax/',views.business_hits_ajax, name='business_hits_ajax'),
]