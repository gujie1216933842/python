from django.shortcuts import render, redirect
from django.http import JsonResponse
import sys
from . import models
from hashlib import sha1
import time


# Create your views here.

class user():
    def login(request):
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
        userinfo = models.UserInfo()
        # 此条代码,django用户查询数据库
        count = userinfo.objects.filter(uname=uname).count()
        return JsonResponse(dict(count=count))
