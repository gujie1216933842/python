# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
import sys
from . import models
from hashlib import sha1
import time
import logging


# Create your views here.

class user():
    def login(request):
        logger = logging.getLogger('django')
        logger.info('This is aerr msg')
        return render(request, 'user/login.html')

    def register(request):
        return render(request, 'user/register.html')

    def register_handler(request):
        # 接收用户输入
        post = request.POST
        uname = post.get('user_name')
        upwd = post.get('pwd')
        cupwd = post.get('cpwd')
        uemail = post.get('email')

        # 判断两次密码是否一致
        if upwd != cupwd:
            return redirect('/user/login')

        # 用户注册信息开始入库
        # 加密用户密码
        sha1_obj = sha1()
        sha1_obj.update(upwd.encode())
        upwd_sha1 = sha1_obj.hexdigest()
        # 创建model用户对象
        user = models.UserInfo()
        user.uname = uname
        user.upwd = upwd_sha1
        user.uemail = uemail
        user.raw_add_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        user.save()
        return redirect('/user/login')

    def register_exist(request):
        get = request.GET
        uname = get.get('uname')
        '''
        以下这种写法代码会报错:Manager isn't accessible via UserInfo instances        
        # count = models.UserInfo().objects.filter(uname=uname).count()
        # 此条代码,django用户查询数据库
        model.UserInfo():表示UserInfo的实例对象
        model.UserInfo:表示UserInfo的类对象
        而模型管理器Manager只是争对与类对象才有的权限        
        '''
        count = models.UserInfo.objects.filter(uname=uname).count()
        print(count)
        return JsonResponse(dict(count=count))

    def login_handler(request):
        # 获取用户的用户名和密码
        post = request.POST
        uname = post.get('username')
        upwd = post.get('pwd')
        jizhu = post.get('jizhu', 0)
        print(jizhu)

        # 实例化
        # 获取加密后的密码
        sha1_obj = sha1()
        sha1_obj.update(upwd.encode())
        sha1_upwd = sha1_obj.hexdigest()
        user = models.UserInfo.objects.filter(uname=uname, upwd=sha1_upwd)
        if user:
            response = HttpResponseRedirect('/goods/')
            if jizhu != 0:
                # 记住用户名勾上的话,如果登录成功,把用户名记录在cookie中
                response.set_cookie('uname', uname)
            else:
                response.set_cookie('uname', '', max_age=-1)  # max_age 超时时间
            # 进入这一步表示已经登录成功了,把用户信息写入session
            request.session['user_id'] = user[0].id
            request.session['user_name'] = user[0].uname
            return response
        else:
            return HttpResponseRedirect('/user/login')



    def ucenter(request):
        return render(request,'user/user_center_info.html')

