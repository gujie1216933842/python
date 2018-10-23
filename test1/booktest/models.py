from django.db import models

status_choices = (
    (0, u'未处理'),
    (2, u'正在生成PDF'),
    (9, u'生成PDF成功'),
)


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    pdfStatus = models.IntegerField(choices=status_choices)

    class Meta:
        db_table = 'bookinfo'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=50)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    # 定义外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')


class image(models.Model):
    image_name = models.CharField(max_length=20, verbose_name='图片名称')
    image_url = models.CharField(max_length=20, verbose_name='图片链接')
