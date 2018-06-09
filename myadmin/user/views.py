from django.shortcuts import render,HttpResponse
from django.views.generic.base import View
from utils.captcha.captcha import Verifycode


class Logout(View):
    def get(self,request):
        return render(request,'user/login.html')








class Captcha(View):
    captcha = Verifycode()
    HttpResponse(captcha)


