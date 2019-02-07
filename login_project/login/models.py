from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='', max_length=100)    #verbose_name을 아이디라고 지정하고 싶은데 모델폼을 써서 자꾸 사이트에서 보인다. 안 예뻐서 공백처리 ㅜㅜ

    def __repr__(self):
        return '{}님의 계정'.format(self.name)
