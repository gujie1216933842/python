from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
import os, sys

# 找到当前目录的路径
file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, file_path)
from utils.captcha.captcha import Verifycode
from . import mymodels


class Logout(View):
    def get(self, request):
        return render(request, 'user/login.html')


class Login(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = mymodels.User()
        ret = user.userLogin(username, password)
        if not ret[0]:
            return redirect('/index/')
        else:
            return HttpResponse('用户名和密码不正确!')


class Captcha(View):
    def get(self, request):
        captcha = Verifycode(140, 40, 4, 33)
        code, image = captcha.getVerifycode()
        return HttpResponse(image, content_type='image/png')
