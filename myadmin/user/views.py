from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
import os, sys

# 找到当前目录的路径
file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, file_path)
from utils.captcha.captcha import Verifycode
from . import mymodels
import requests
from . import models
from hashlib import sha1
from django.conf import settings


class Logout(View):
    def get(self, request):
        request.session['login'] = 'loginvalue'
        return render(request, 'user/login.html')


class Login(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # 密码sha1加密
        sha1_obj = sha1()
        password_secret = "%s%s" % (password, settings.PRIVATE_KEY)
        sha1_obj.update(password_secret.encode())
        password_sha1 = sha1_obj.hexdigest()
        userItem = models.UserInfo.objects.filter(username=username, password=password_sha1)

        #把信息用户名和密码信息存入session中,如果使用django,则需要migration
        request.session['username'] = username
        request.session.set_expiry(5)
        '''
        把sessionstore对象打印出来,程序调试过程中会用到
        print(dict(request.session))
        删除session
        del request[key]
        
        '''



        if userItem:
            return redirect('/index/')
        else:
            return HttpResponse('用户名和密码不正确!')


class Captcha(View):
    def get(self, request):
        captcha = Verifycode(140, 40, 4, 33)
        code, image = captcha.getVerifycode()
        return HttpResponse(image, content_type='image/png')
