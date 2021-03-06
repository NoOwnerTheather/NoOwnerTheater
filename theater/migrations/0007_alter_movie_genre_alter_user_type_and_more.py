# Generated by Django 4.0.2 on 2022-02-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0006_alter_movie_comeout_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('멜로/로맨스', '멜로/로맨스'), ('뮤지컬', '뮤지컬'), ('SF', 'SF'), ('범죄', '범죄'), ('미스터리', '미스터리'), ('애니메이션', '애니메이션'), ('공포(호러)', '공포(호러)'), ('액션', '액션'), ('코미디', '코미디'), ('드라마', '드라마'), ('사극', '사극'), ('다큐멘터리', '다큐멘터리'), ('스릴러', '스릴러'), ('판타지', '판타지'), ('가족', '가족'), ('성인물(에로)', '성인물(에로)'), ('전쟁', '전쟁')], max_length=100, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('일반 사용자', '일반 사용자'), ('제작사', '제작사')], max_length=20, verbose_name='가입 유형'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_img',
            field=models.TextField(default='/static/img/user4.PNG', verbose_name='유저사진'),
        ),
    ]
