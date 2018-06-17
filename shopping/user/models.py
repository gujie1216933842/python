from django.db import models

# Create your models here.


Type = {
    '1': '新',
    '2': '老',
    '3': '外联用户',
}


class UserInfo(models.Model):
    # 以下数据库的字段定义一定要加
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    type = models.CharField(choices=Type, max_length=30)
    raw_add_time = models.DateTimeField()
