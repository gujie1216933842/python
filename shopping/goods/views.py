from django.shortcuts import render
from . import models


# Create your views here.

# 控制器中以方法的方式
# def index(request):
#     return  render(request,'goods/index.html')


# 控制器中以类的方式
class goods():
    def index(request):
        # 显示首页信息
        # 时令水果
        res1 = models.goods.objects.fliter(delete_flag=0)
        return render(request, 'goods/index.html', {'guest_cart': 1, 'res1': res1})

    def detail(request):
        return render(request, 'goods/detail.html')
