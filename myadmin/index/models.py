from django.db import models


# Create your models here.


class TopResorce(models.Model):
    '''
    default只是针对于用resource对象时,才有作用
    migration的时候在数据库中迁移,字段后面不会出现default
    资源管理表
    '''
    name = models.CharField(max_length=10, null=False, default='')
    link = models.CharField(max_length=50, null=False, default='')
    delete_flag = models.BooleanField(null=False, default=False)
    raw_add_time = models.DateTimeField(auto_now_add=True, null=False)
    raw_update_time = models.DateTimeField(auto_now=True)













class Resource(models.Model):
    '''
    default只是针对于用resource对象时,才有作用
    migration的时候在数据库中迁移,字段后面不会出现default
    资源管理表
    '''
    name = models.CharField(max_length=10, null=False, default='')
    link = models.CharField(max_length=50, null=False, default='')
    delete_flag = models.BooleanField(null=False, default=False)

    raw_add_time = models.DateTimeField(auto_now_add=True, null=False)
    raw_update_time = models.DateTimeField(auto_now=True)


class Catalog(models.Model):
    '''
    目录管理表
    '''
    name = models.CharField(max_length=10, null=False, default='')
    delete_flag = models.BooleanField(null=False, default=False)
    raw_add_time = models.DateTimeField(auto_now_add=True, null=False)
    raw_update_time = models.DateTimeField(auto_now=True)


class ResourceCatalog(models.Model):
    '''
    资源和目录关系表
    '''
    resource_id = models.IntegerField(null=False, default=0)
    catalog_id = models.IntegerField(null=False, default=0)
    delete_flag = models.BooleanField(null=False, default=False)
    raw_add_time = models.DateTimeField(auto_now_add=True, null=False)
    raw_update_time = models.DateTimeField(auto_now=True)


class UserResource(models.Model):
    '''
    资源和用户id关系表
    '''
    user_id = models.IntegerField(null=False, default=0)
    resource_id = models.IntegerField(null=False, default=0)
    delete_flag = models.BooleanField(null=False, default=False)
    raw_add_time = models.DateTimeField(auto_now_add=True, null=False)
    raw_update_time = models.DateTimeField(auto_now=True)
