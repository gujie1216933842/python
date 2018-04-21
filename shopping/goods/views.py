from django.shortcuts import render
from . import models


# Create your views here.

# 控制器中以方法的方式
# def index(request):
#     return  render(request,'goods/index.html')


# 控制器中以类的方式
class goods():
    fun1 = ''

    def __init__(self, request):
        self.fun1 = goods()

    def index(self,request):
        # 显示首页信息
        # 时令水果
        res1 = models.goods.objects.filter(delete_flag=0)
        res1 = self.fun1.float_control(res1)

        return render(request, 'goods/index.html', {'guest_cart': 1, 'res1': res1})

    def detail(request):
        return render(request, 'goods/detail.html')

    def float_control(res, decimal_count=2):
        for i in res:
            res[i] = round(res['price'], decimal_count)
        return res
