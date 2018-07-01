from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
import os, sys, json, random, time, datetime

# 找到当前目录的路径
file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, file_path)
from utils.captcha.captcha import Verifycode
from utils.common import django_model_opration
from . import mymodels, models
import requests
from . import models
from hashlib import sha1, md5
from django.conf import settings
from django.core.cache import cache
from django.core.serializers import serialize


class Logout(View):
    def get(self, request):
        request.session['login'] = 'loginvalue'
        # 生成一个随机数字,这里用时间戳来替换
        return redirect('/user/login/')


class Login(View):

    def get(self, request):
        '''
        显示登录页面
        '''
        random_num = int(time.time())
        return render(request, 'user/login.html', {'random_num': random_num})

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        captcha = request.POST.get('captcha', '')
        captcha_key = request.POST.get('captcha_key', '')

        # 检查验证码是否正确
        # redis中获取的验证码
        cache_captcha = cache.get("captcha_%s" % captcha_key)
        print('前端页面传过来的%s' % captcha)
        print('缓存中取得值%s' % cache_captcha)
        if cache_captcha is None:
            return HttpResponse({'code': '01', 'msg': '验证码已经过期,请刷新后重新输入!'})

        if captcha != cache_captcha:
            return HttpResponse({'code': '02', 'msg': '验证码不正确,请重新输入!'})

        # 密码sha1加密
        sha1_obj = sha1()
        password_secret = "%s%s" % (password, settings.PRIVATE_KEY)
        sha1_obj.update(password_secret.encode())
        password_sha1 = sha1_obj.hexdigest()
        userItem = models.UserInfo.objects.filter(username=username, password=password_sha1).all()

        if userItem:
            # 把信息用户名和密码信息存入session中,如果使用django,则需要migration
            '''
            把sessionstore对象打印出来,程序调试过程中会用到
            print(dict(request.session))
            删除session
            del request[key]
            '''
            userInfo = dict(username=username, userId=userItem[0].id)
            request.session['userInfo'] = userInfo
            return HttpResponse({'code': '00', 'msg': '登录成功!'})
        else:
            return HttpResponse({'code': '02', 'msg': '用户名或密码不正确,请重新输入!'})


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


class UserList(View):
    def get(self, request):
        return render(request, 'user/user_list.html')

    def post(self, request):
        '''
        1.查询所有数据
        '''

        page = request.POST.get('page', 1)
        rows = request.POST.get('rows', 10)
        page = int(page)
        rows = int(rows)
        start = rows * (page - 1)
        end = start + rows - 1
        userItems = models.UserInfo.objects.all()[start: end]
        useList = django_model_opration(userItems)
        count = models.UserInfo.objects.all().count()
        user_dict = dict(rows=useList, total=count)
        return HttpResponse(json.dumps(user_dict))


class UserAdd(View):
    def get(self, request):
        return render(request, 'user/user_add.html')

    def post(self, request):
        '''
        添加数据接口
        1.获取数据
        2.数据入口

        '''
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        gender = request.POST.get('gender', '')

        print('username:%s' % username)
        print('password:%s' % password)
        print('gender:%s' % gender)

        # 密码处理
        '''
        1.md5加密
        2.拼接秘钥
        3.sha1加密
        '''
        md5_obj = md5()
        md5_obj.update(password.encode())
        password = md5_obj.hexdigest()
        password = "%s%s" % (password, settings.PRIVATE_KEY)

        sha1_obj = sha1()
        sha1_obj.update(password.encode())
        password = sha1_obj.hexdigest()  # 返回摘要，作为十六进制数据字符串值

        # 实例化对象
        userInfo = models.UserInfo()
        userInfo.username = username
        userInfo.password = password
        userInfo.save()

        return HttpResponse('add ok!')
