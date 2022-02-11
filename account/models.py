from django.db import models
from pickle import FALSE
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import requests
from random import randint
from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class AuthSMS(TimeStampedModel):
    phone_number = models.CharField(verbose_name='휴대폰 번호', primary_key=True, max_length=11)
    auth_number = models.IntegerField(verbose_name='인증 번호')
    class Meta:
        db_table = 'auth_user'

    def save(self, *args, **kwargs):
        self.auth_number = randint(1000, 10000)
        super().save(*args, **kwargs)
        self.send_sms() # 인증번호가 담긴 SMS를 전송

    def send_sms(self):
        url = 'https://api-sens.ncloud.com/v1/sms/services/{serviceId}/messages/'
        data = {
                "type": "SMS",
                "from": "01012345678",
                "to": [self.phone_number],
                "content": "[테스트] 인증 번호 [{}]를 입력해주세요.".format(self.auth_number)
            }
        headers = {
                "Content-Type": "application/json",
                "x-ncp-auth-key": {"Sub Account Access Key"},
                "x-ncp-service-secret": {"SMS Service Secret"},
            }
        requests.post(url, json=data, headers=headers)
    @classmethod
    def check_auth_number(cls, p_num, c_num):
        time_limit = timezone.now() - datetime.timedelta(minutes=5)
        result = cls.objects.filter(
            phone_number=p_num,
            auth_number=c_num,
            modified__gte=time_limit
            )
        if result:
            return True
        return False

    
    