from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
import os, sys, json, random, time, datetime

from utils.captcha.captcha import Verifycode
from utils.common import django_model_opration

import requests
from . import models
from hashlib import sha1, md5
from django.conf import settings
from django.core.cache import cache
from django.core.serializers import serialize
from rediscache.views import getCache
from django.http import JsonResponse


class Test(View):
    def get(self, request):
        return getCache(request)


class Logout(View):
    def get(self, request):
        request.session['userInfo'] = ''
        # 生成一个随机数字,这里用时间戳来替换
        return redirect('/user/login/')


class Login(View):

    def get(self, request):
        '''
        显示登录页面
        '''
        return render(request, 'user/login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        captcha = request.POST.get('captcha', '')
        captcha_key = request.POST.get('captcha_key', '')

        if not captcha:
            resp = {'code': '01', 'msg': '请输入图片验证码!'}
            return HttpResponse(json.dumps(resp))

        # 检查验证码是否正确
        # redis中获取的验证码
        cache_captcha = cache.get("captcha_%s" % captcha_key)
        print('前端页面传过来的%s' % captcha)
        print('缓存中取得值%s' % cache_captcha)
        if cache_captcha is None:
            resp = {'code': '02', 'msg': '验证码已经过期,请刷新后重新输入!'}
            return HttpResponse(json.dumps(resp))

        if captcha != cache_captcha:
            resp = {'code': '03', 'msg': '验证码不正确,请重新输入!'}
            return HttpResponse(json.dumps(resp))

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
            resp = {'code': '00', 'msg': '登录成功!'}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'code': '04', 'msg': '用户名或密码不正确,请重新输入!'}
            return HttpResponse(json.dumps(resp))


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
        search_username = request.POST.get('search_username', '')

        page = int(page)
        rows = int(rows)
        start = rows * (page - 1)
        end = start + rows - 1

        if search_username:
            userItems = models.UserInfo.objects.filter(delete_flag=False, username__contains=search_username).order_by(
                '-id')[start: end]
            useList = django_model_opration(userItems)
            count = models.UserInfo.objects.filter(delete_flag=False, username__contains=search_username).count()
        else:
            userItems = models.UserInfo.objects.filter(delete_flag=False).order_by('-id')[start: end]
            useList = django_model_opration(userItems)
            count = models.UserInfo.objects.filter(delete_flag=False).count()
        user_dict = dict(rows=useList, total=count)
        return HttpResponse(json.dumps(user_dict))


class UserAdd(View):

    def post(self, request):
        '''
        添加数据接口
        1.获取数据
        2.数据入口

        '''
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # 密码处理
        '''
        1.md5加密
        2.拼接秘钥
        3.sha1加密
        '''
        if confirm_password != password:
            resp = {'code': '01', 'msg': '密码与确认密码不一致,请重新输入!'}
            return HttpResponse(json.dumps(resp))

        # 判断用户名是否已经在数据库中存在
        count = models.UserInfo.objects.filter(username=username).count()
        if count >= 1:
            resp = {'code': '02', 'msg': '用户名已经存在,请重新输入!'}
            return HttpResponse(json.dumps(resp))

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

        resp = {'code': '00', 'msg': '添加成功!'}
        return HttpResponse(json.dumps(resp))


class UserEdit(View):

    def post(self, request):
        '''
        添加数据接口
        1.获取数据
        2.数据入口

        '''
        id = request.POST.get('id', '')
        username = request.POST.get('username', '')
        old_password = request.POST.get('old_password', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        compare_password = old_password
        # 查询id对应的数据库密码是否与老密码相等
        # md5,sha1加密处理老密码
        md5_obj = md5()
        md5_obj.update(old_password.encode())
        old_password = md5_obj.hexdigest()
        old_password = "%s%s" % (old_password, settings.PRIVATE_KEY)

        sha1_obj = sha1()
        sha1_obj.update(old_password.encode())
        old_password = sha1_obj.hexdigest()  # 返回摘要，作为十六进制数据字符串值
        # 通过id查询老密码
        model_password_obj = models.UserInfo.objects.filter(id=id).values("password")[0]
        model_password = model_password_obj['password']

        if model_password != old_password:
            resp = {'code': '01', 'msg': '原密码不正确,请重新输入!'}
            return HttpResponse(json.dumps(resp))

        # 判断新密码和老密码是否一致
        if password == compare_password:
            resp = {'code': '02', 'msg': '新密码与老密码应不一致,请重新输入!'}
            return HttpResponse(json.dumps(resp))

        # 判断两次输入的新密码是否一致
        if password != confirm_password:
            resp = {'code': '03', 'msg': '两次输入的新密码不一致,请重新输入!'}
            return HttpResponse(json.dumps(resp))

        # 加密新密码
        new_password = password
        # md5,sha1加密处理老密码
        md5_obj = md5()
        md5_obj.update(new_password.encode())
        new_password = md5_obj.hexdigest()
        new_password = "%s%s" % (new_password, settings.PRIVATE_KEY)

        sha1_obj = sha1()
        sha1_obj.update(new_password.encode())
        new_password = sha1_obj.hexdigest()  # 返回摘要，作为十六进制数据字符串值

        # 更新密码和用户名
        try:
            # 当前时间
            raw_update_time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            models.UserInfo.objects.filter(id=id).update(username=username, password=new_password,
                                                         raw_update_time=raw_update_time)
        except Exception as  e:
            print('编辑异常:%s' % e)
            resp = {'code': '04', 'msg': '编辑失败!'}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'code': '00', 'msg': '编辑成功!'}
            return HttpResponse(json.dumps(resp))


class UserDel(View):
    def post(self, request):
        id = request.POST.get('id', '')
        raw_update_time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        try:
            models.UserInfo.objects.filter(id=id).update(delete_flag=True, raw_update_time=raw_update_time)
        except Exception as e:
            resp = {'code': '01', 'msg': '删除失败!'}
            return JsonResponse(resp)
        resp = {'code': '01', 'msg': '删除成功!'}
        return JsonResponse(resp)
