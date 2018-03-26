from django.db import models


# Create your models here.

class bookInfo(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField()


class heroInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    content = models.CharField(max_length=1000)
    book = models.ForeignKey(bookInfo)
