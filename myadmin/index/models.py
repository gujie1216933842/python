from django.db import models


# Create your models here.
type = (
    (1, "系统管理"),
    (2, "游戏管理"),
    (3, "商城管理"),
    (4, "爬虫管理"),
    (5, "数据分析"),
)


class Resource(models.Model):
    '''
    default只是针对于用resource对象时,才有作用
    migration的时候在数据库中迁移,字段后面不会出现default
    资源管理表
    '''
    name = models.CharField(max_length=50, null=False, default='')
    link = models.CharField(max_length=50, null=False, default='')
    category = models.PositiveIntegerField(choices=type,null=False,)
    delete_flag = models.BooleanField(null=False, default=False)
    raw_add_time = models.DateTimeField(auto_now_add=True, null=False)
    raw_update_time = models.DateTimeField(auto_now=True)


