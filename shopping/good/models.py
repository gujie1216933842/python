from django.db import models


# Create your models here.

class good(models.Model):
    # 定义商品字段
    name = models.CharField(max_length=20, null=False , default="")
    price = models.FloatField(null=False,default='')
    #pic = models.CharField(max_length=50, null=False ,default="")
    pic = models.ImageField(upload_to='/statics/gooodsImage')

    detail_pic = models.CharField(max_length=50, null=False ,default="")
    unit = models.CharField(max_length=20, null=False ,default="")
    raw_add_time = models.DateTimeField(auto_now_add=True)
    raw_update_time = models.DateTimeField(auto_now=True)
    delete_flag = models.BooleanField(null=False,default=0)

