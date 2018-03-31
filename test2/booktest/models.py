from django.db import models

# Create your models here.
'''
自定义模型管理器
'''


class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    '''
    在自定义,模型管理器中自定义创建方法,类似与__init__,注意,不能用__init__
    django官方推荐使用
    '''
    def create_obj(cls, btitle, bpub_date):
        obj = BookInfo()
        obj.btitle = btitle
        obj.bpub_date = bpub_date
        obj.bread = 0
        obj.bcomment = 0
        obj.isDelete = False
        return obj


class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    class Mrta:
        db_table = "bookinfo"

    bookinfo1 = models.Manager()  # django自己生成模型管理器
    bookinfo2 = BookInfoManager()  # 自定义的模型类管理器
    '''
    模型类自定义创建方法,类似与__init__,注意,不能用__init__
    '''

    @classmethod
    def create_obj(cls, btitle, bpub_date):
        obj = BookInfo()
        obj.btitle = btitle
        obj.bpub_date = bpub_date
        obj.bread = 0
        obj.bcomment = 0
        obj.isDelete = False
        return obj

    '''
    在其他地方调用
    from booktest2.model import BookInfo
    from datetime import datetime
    b = BookInfo.books2.create('鹿鼎记'.datetime(2018,1,3))
    b.save()
    执行完之后,去数据库中查看数据是否已经添加
    '''


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)
