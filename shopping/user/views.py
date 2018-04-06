from django.shortcuts import render,redirect
import sys
from . import models
# Create your views here.

class user():
    def login(request):
        return render(request, 'user/login.html')

    def register(request):
        return render(request, 'user/register.html')


    def register_handler(request):
        #接收用户输入
        post = request.POST
        uname = post.get('user_name')
        upwd = post.get('pwd')
        cupwd = post.get('cpwd')
        uemail = post.get('email')

        #判断两次密码是否一致
        if upwd !=cupwd:
            return redirect('/user/login')
        #创建model用户对象
        user= models.UserInfo()
        




    def register_exist(request):
        post = request.POST
        uname = post.get('user_name')
        print(uname)
        #sys.exit





