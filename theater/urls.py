from django.urls import path
from . import views

app_name = 'theater'

urlpatterns = [
   path('', views.main, name='main'),
   path('preview/',views.preview,name="preview"), #시사회 페이지
   path('preview/<int:pk>/',views.preview_detail,name='preview_detail'), #시사회 디테일페이지

   #path('preview/<int:pk>/comments/', views.comments_create, name='comments_create'),



   #path('preview/<int:pk>/comment/write/', views.comment_write_view, name='comment_write'),
   #path('preview/<int:pk>/comment/delete/', views.comment_delete_view, name='comment_delete'),

   path('preview/<int:pk>/like_ajax/', views.like_ajax, name='like_ajax'),

   path("preview/<int:pk>/write_comment/", views.write_comment, name='write_comment'),
   path("preview/<int:pk>/del_comment/", views.del_comment, name='del_comment'),


]