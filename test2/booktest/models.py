from django.db import models

# Create your models here.

class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment=models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Mrta:
        db_table = "bookinfo"

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)
    
