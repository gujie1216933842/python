from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views.generic.base import View

'''函数方法'''
# def send(request):
#     msg = '<a href="http://www.baidu.com" target="_blank">点击激活</a>'
#     send_mail('测试邮件', '', settings.EMAIL_FROM, ['1216933842@qq.com'], msg)
#     return HttpResponse('ok')

'''类方法'''
class sendHandler(View):

    def get(self, request):
        msg = '<a href="http://www.baidu.com" target="_blank">点击激活</a>'
        send_mail('测试邮件', '', settings.EMAIL_FROM, ['1216933842@qq.com'], msg)
        return HttpResponse('ok')

