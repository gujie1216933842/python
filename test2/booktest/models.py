from django.db import models
from datetime import datetime


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    age = models.IntegerField(default=0, verbose_name=u'年龄')
    hobby = models.CharField(max_length=20, verbose_name=u'爱好')
    # add_time = models.DateTimeField( auto_now_add=True, verbose_name=u'添加时间')
    # update_time = models.DateTimeField( auto_now=True, verbose_name=u'更新时间')

    class Meta:
        # db_table = 'booktest_user'
        verbose_name = u'用户'
        verbose_name_plural = verbose_name



class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    age = models.IntegerField(default=0, verbose_name=u'年龄')
    hobby = models.CharField(max_length=20, verbose_name=u'爱好')
    add_time = models.DateTimeField( auto_now_add=True, verbose_name=u'添加时间')
    update_time = models.DateTimeField( auto_now=True, verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'学生'
        verbose_name_plural = verbose_name


class NewStudent(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    age = models.IntegerField(default=0, verbose_name=u'年龄')
    hobby = models.CharField(max_length=20, verbose_name=u'爱好')
    add_time = models.DateTimeField( auto_now_add=True, verbose_name=u'添加时间')
    update_time = models.DateTimeField( auto_now=True, verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'学生'
        verbose_name_plural = verbose_name


