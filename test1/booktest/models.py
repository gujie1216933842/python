from django.db import models

# Create your models here.
class booInfo(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField

class heroInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.BooleanField()
    content = models.CharField(max_length=1000)
    #定义外键
    book = models.ForeignKey(booInfo)

