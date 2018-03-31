from django.db import models

# Create your models here.
'''
自定义模型管理器
'''


class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)


class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    class Mrta:
        db_table = "bookinfo"

    bookinfo1 = models.Manager()  # django自己生成的模型类对象
    bookinfo2 = BookInfoManager()  # 自定义的模型类对象
    '''
    自定义模型类创建方法,类似与__init__,注意,不能用__init__
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


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)
