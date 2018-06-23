from django.db import models


# Create your models here.


class resource(models.Model):
    '''
    default只是针对于用resource对象时,才有作用
    migration的时候在数据库中迁移,字段后面不会出现default
    '''
    name = models.CharField(max_length=10, null=False, default='')
    link = models.CharField(max_length=50, null=False, default='')
    delete_flag = models.BooleanField(null=False, default=False)
    raw_add_time = models.DateTimeField(auto_now_add=True, null=False)
    raw_update_time = models.DateTimeField(auto_now=True)



