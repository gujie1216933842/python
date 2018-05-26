from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def send(request):
    msg = '<a href="http://www.baidu.com" target="_blank">点击激活</a>'
    send_mail('测试邮件', '', settings.EMAIL_FROM, ['1216933842@qq.com'], msg)
    return HttpResponse('ok')




# Create your views here.

# 控制器中以方法的方式
# def index(request):
#     return  render(request,'good/index.html')
# class send(View):
#
#     def get(self, request):
#         msg = '<a href="http://www.baidu.com" target="_blank">点击激活</a>'
#         send_mail('测试邮件', '', settings.EMAIL_FROM, ['1216933842@qq.com'], msg)
#         return HttpResponse('ok')

    # 　return HttpResponse('ok')
