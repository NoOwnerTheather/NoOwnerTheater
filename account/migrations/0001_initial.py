# Generated by Django 4.0.2 on 2022-02-16 13:19

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthSMS',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('phone_number', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='휴대폰 번호')),
                ('auth_number', models.IntegerField(verbose_name='인증 번호')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
    ]
