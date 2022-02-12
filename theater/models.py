from django.db import models
from django.contrib.auth.models import AbstractUser
from random import *
import random

# Create your models here.
TYPE_CHOICE = {('일반 사용자', '일반 사용자'), ('제작사', '제작사')}
GENDER_CHOICE = {('남자', '남자'), ('여자', '여자')}
class User(AbstractUser):

    IMG_CHOICE = ['imgs/1.PNG','imgs/2.PNG','imgs/3.PNG','imgs/4.PNG','imgs/5.PNG'] ###추가한부분

    img=random.choice(IMG_CHOICE) ###추가한부분

    nickname = models.CharField(verbose_name='닉네임', max_length=20)
    phone = models.CharField(verbose_name='휴대폰 번호', max_length=20)
    type = models.CharField(verbose_name='가입 유형', choices=TYPE_CHOICE, max_length=20)
    mileage = models.IntegerField(verbose_name='마일리지', default=0)
    gender = models.CharField(verbose_name='성별', choices=GENDER_CHOICE, max_length=20)

    user_img = models.FileField(default=img, verbose_name="유저사진") ###추가한부분


GENRE_CHOICE = {('액션', '액션'), ('애니메이션', '애니메이션'), ('드라마', '드라마'), ('스릴러', '스릴러'), ('코미디', '코미디'), ('멜로/로맨스', '멜로/로맨스'), ('범죄', '범죄'), ('공포(호러)', '공포(호러)'), ('미스터리', '미스터리'), ('성인물(에로)', '성인물(에로)'), ('SF', 'SF'), ('사극', '사극'), ('판타지', '판타지'), ('전쟁', '전쟁'), ('다큐멘터리', '다큐멘터리'), ('뮤지컬', '뮤지컬'), ('가족', '가족')}
# GRADE_CHOICE = {('전체 관람가', '전체 관람가'), ('12세', '12세'), ('15세', '15세'), ('청소년 관람불가', '청소년 관람불가')}
COMEOUT_CHOICE={('개봉','개봉'),('미개봉 및 제작중','미개봉 및 제작중')}
class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) ###추가한부분
    title = models.CharField(verbose_name='제목', max_length=50)
    genre = models.CharField(verbose_name='장르', choices=GENRE_CHOICE, max_length=100)
    running_time = models.IntegerField(verbose_name='러닝타임',null=True)
    release_date = models.DateField(verbose_name='개봉')
    director = models.CharField(verbose_name='감독', max_length=50)
    actor = models.CharField(verbose_name='배우', max_length=100)
    content = models.TextField(verbose_name='개요',null=True)
    # grade = models.CharField(verbose_name='등급', choices=GRADE_CHOICE, max_length=20)
    # company = models.CharField(max_length=50 ,verbose_name='배급사') 배급사는 제작사 유저로 하면 될 것 같아!
    rating = models.FloatField(verbose_name='평점', default=0)
    poster = models.ImageField(upload_to="poster/", null=True, blank=True, verbose_name="포스터")
    video = models.FileField(upload_to='videos/', null=True, blank=True, verbose_name="예고편")
    url= models.URLField(verbose_name='링크',null=True)
    comeout=models.CharField(verbose_name="개봉여부",choices=COMEOUT_CHOICE,max_length=100)
    def __str__(self):
        return str(self.title)

# class UnreleasedMovie(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50 ,verbose_name='제목')
#     genre = models.CharField(choices= GENRE_CHOICE, verbose_name='장르', max_length=100)
#     director = models.CharField(max_length=50,verbose_name='감독', null=True, blank=True)
#     actor = models.CharField(max_length=100,verbose_name='출연', null=True, blank=True)
#     intro = models.TextField(verbose_name='소개')
#     grade = models.CharField(choices= GRADE_CHOICE, verbose_name='등급', null=True, blank=True, max_length=20)
#     company = models.CharField(max_length=50 ,verbose_name='배급사')
#     poster = models.ImageField(upload_to="poster/", null=True, blank=True, verbose_name="포스터")
#     budget_detail = models.TextField(verbose_name='예산')
#     schedule_detail = models.TextField(verbose_name='일정')
#     company_detail = models.TextField(verbose_name='제작사 소개')
#     gift = models.TextField(verbose_name='선물 설명')
#     money = models.IntegerField(verbose_name='펀딩 금액', default=0)
    
#     def __str__(self):
#         return str(self.title)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='한 줄 제목', max_length=200)
    content = models.TextField(verbose_name='내용')
    rating = models.IntegerField(verbose_name='평점')
    like = models.IntegerField(verbose_name='좋아요', default=0)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    def __str__(self):
        return str(self.title)

class CommentReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

class CommentPreview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) 
    content = models.TextField(verbose_name='내용')
    like = models.IntegerField(verbose_name='좋아요', default=0)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField(verbose_name='내용')
    hits = models.IntegerField(verbose_name='조회수', default=0)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    image=models.ImageField(upload_to="poster/", null=True, blank=True, verbose_name="이미지")
    def __str__(self):
        return str(self.title)


    

    