# Generated by Django 4.0.2 on 2022-02-07 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('SF', 'SF'), ('스릴러', '스릴러'), ('드라마', '드라마'), ('판타지', '판타지'), ('가족', '가족'), ('전쟁', '전쟁'), ('미스터리', '미스터리'), ('성인물(에로)', '성인물(에로)'), ('공포(호러)', '공포(호러)'), ('애니메이션', '애니메이션'), ('액션', '액션'), ('범죄', '범죄'), ('코미디', '코미디'), ('뮤지컬', '뮤지컬'), ('멜로/로맨스', '멜로/로맨스'), ('다큐멘터리', '다큐멘터리'), ('사극', '사극')], max_length=100, verbose_name='장르'),
        ),
    ]