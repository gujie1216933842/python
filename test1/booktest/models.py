from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=50)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    # 定义外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
