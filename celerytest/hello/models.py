from django.db import models


# Create your models here.

class Add(models.Model):
    task_id = models.CharField(max_length=128)
    first = models.IntegerField()  # 存储第一个加数
    second = models.IntegerField()  # 存储第二个加数
    log_date = models.DateTimeField()  # 存储开始时间
