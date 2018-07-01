from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    raw_add_time = models.DateTimeField(auto_now_add=True)  # 用于记录添加时间
    raw_update_time = models.DateTimeField(auto_now=True)  # 用于更新
