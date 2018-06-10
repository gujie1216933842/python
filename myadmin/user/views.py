from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
import os, sys

# 找到当前目录的路径
file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, file_path)
from utils.captcha.captcha import Verifycode


class Logout(View):
    def get(self, request):
        return render(request, 'user/login.html')


class Captcha(View):
    def get(self, request):
        captcha = Verifycode(200, 40, 4)
        return HttpResponse(captcha.getVerifycode())
