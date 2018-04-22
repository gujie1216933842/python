from django.shortcuts import render
from . import models
from django.views.generic.base import View


# Create your views here.

# 控制器中以方法的方式
# def index(request):
#     return  render(request,'goods/index.html')


# 控制器中以类的方式
class goods(View):

    def get(self, request):
        # 显示首页信息
        # 时令水果
        res1 = models.goods.objects.filter(delete_flag=0)
        res1 = self.float_control(res1)

        return render(request, 'goods/index.html', {'guest_cart': 1, 'res1': res1})

    def detail(self, request):
        return render(request, 'goods/detail.html')

    def float_control(self, res, ndigits=2):
        new_res = []
        for k,v in res:
            res[k] = round(v.price, ndigits)
        return res
