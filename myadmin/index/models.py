from django.db import models


# Create your models here.


class resource(models.Model):
    name = models.CharField(max_length=10, null=False, default='', db_column='资源名称')
    link = models.CharField(max_length=50, null=False, default='', db_column='资源链接')
    delete_flag = models.BooleanField(null=False, default=False, db_column='记录是否删除,0:否,1:删除')
    raw_add_time = models.DateTimeField(auto_now_add=True, db_column='记录添加时间')
