from django.shortcuts import render
from . import models
from django.views.generic.base import View
import logging

# Create your views here.

# 控制器中以方法的方式
# def index(request):
#     return  render(request,'goods/index.html')


# 控制器中以类的方式
class goodsIndex(View):
    def get(self, request):
        # 显示首页信息
        # 时令水果
        res1 = models.goods.objects.filter(delete_flag=0)
        res1 = self.float_control(res1)
        return render(request, 'goods/index.html', {'guest_cart': 1, 'res1': res1,'title':'首页'})

    def float_control(self, res, ndigits=2):
        for i in range(len(res)):
            res[i].price = round(res[i].price, ndigits)
        return res


class goodsDatail(View):
    def get(self, request):
        goods_id = request.GET.get('goods_id', 1)
        # 根据goods_id去查数据库
        ret = models.goods.objects.filter(id=goods_id, delete_flag=0)
        ret = goodsIndex().float_control(ret)
        '''
        此处总结:  ret = goodsIndex().float_control(ret)  需要实例化,所以要加()
                 和ret = goodsIndex.float_control(ret) 报错
        '''
        print(ret[0].__dict__)
        logger().createLoder().info(ret[0])
        return render(request, 'goods/detail.html', {"goods": ret[0]})

class logger(View):
    def createLoder(self):
        logger = logging.getLogger('django')
        return logger