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
        msg = '<a href="http://www.baidu.com" target="_blank">hello , my name is 小熊</a>'
        try:
            send_mail('来自小熊linux的邮件', msg, settings.EMAIL_FROM, ['1216933842@qq.com'])
        except Exception as e:
            return_msg = '邮件发送异常:%s' % e
        else:
            return_msg = '邮件发送成功!'
        return HttpResponse(return_msg)
