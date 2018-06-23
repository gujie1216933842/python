from django.db import models


# Create your models here.


class resource(models.Model):
    name = models.CharField(u'资源名称', default='', max_length=10, null=False)
    link = models.CharField(u'资源连接', max_length=50, null=False, default='')
    delete_flag = models.BooleanField(u'记录是否删除标记,0:否,1:是', null=False, default=True)
    raw_add_time = models.DateTimeField(u'记录添加时间', auto_now_add=True)

