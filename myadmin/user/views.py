from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
import os, sys, json, random, time

# 找到当前目录的路径
file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, file_path)
from utils.captcha.captcha import Verifycode
from . import mymodels
import requests
from . import models
from hashlib import sha1
from django.conf import settings
from django.core.cache import cache


class Logout(View):
    def get(self, request):
        request.session['login'] = 'loginvalue'
        # 生成一个随机数字,这里用时间戳来替换
        random_num = int(time.time())
        return render(request, 'user/login.html', {'random': random})


class Login(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        captcha = request.POST.get('captcha', '')
        captcha_key = request.POST.get('captcha_key', '')

        # 检查验证码是否正确
        # redis中获取的验证码
        cache_captcha = cache.get(captcha_key)
        if captcha is None:
            return HttpResponse('验证码已经过期,请刷新后重新输入!')
        elif captcha != cache_captcha.encode():
            return HttpResponse('验证码不正确!,请重新输入')

        # 密码sha1加密
        sha1_obj = sha1()
        password_secret = "%s%s" % (password, settings.PRIVATE_KEY)
        sha1_obj.update(password_secret.encode())
        password_sha1 = sha1_obj.hexdigest()
        userItem = models.UserInfo.objects.filter(username=username, password=password_sha1)

        if userItem:
            # 把信息用户名和密码信息存入session中,如果使用django,则需要migration
            '''
            把sessionstore对象打印出来,程序调试过程中会用到
            print(dict(request.session))
            删除session
            del request[key]
            '''
            userInfo = dict(username=username, userId=userItem[0]['id'])
            request.session['userInfo'] = json.loads(userInfo)
            return redirect('/index/')
        else:
            return HttpResponse('用户名和密码不正确!')


class Captcha(View):
    def get(self, request):
        random_num = request.GET.get('random', '')
        captcha = Verifycode(140, 40, 4, 33)
        code, image = captcha.getVerifycode()
        '''
        把code存入redis
        '''
        cache.set('captcha_%s' % random_num, code, settings.CAPTCHA_TIMEOUT)
        return HttpResponse(image, content_type='image/png')
