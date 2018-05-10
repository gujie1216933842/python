from django.db import models


# Create your models here.

class good(models.Model):
    # 定义商品字段
    name = models.CharField(max_length=20, null=False , default="")
    price = models.FloatField(null=False,default='')
    #pic = models.CharField(max_length=50, null=False ,default="")
    pic = models.ImageField(u'首页图片',upload_to='static/images/')
    '''
    u"含有中文字符组成的字符串。
    作用：后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，
    防止因为源码储存格式问题，导致再次使用时出现乱码。说了那么多,其实也可以不加,哈哈哈哈哈哈

     例：r""
　　 作用：声明后面的字符串是普通字符串，相对的，特殊字符串中含有：转义字符  什么什么的。

     b'ssss'  python3中字符串是bytes格式

    '''
    #detail_pic = models.CharField(max_length=50, null=False ,default="")
    detail_pic = models.CharField(u'详情图片',upload_to='static/images/')

    unit = models.CharField(max_length=20, null=False ,default="")
    raw_add_time = models.DateTimeField(auto_now_add=True)
    raw_update_time = models.DateTimeField(auto_now=True)
    delete_flag = models.BooleanField(null=False,default=0)

