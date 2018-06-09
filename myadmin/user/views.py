from django.shortcuts import render,HttpResponse
from django.views.generic.base import View

class Logout(View):
    def get(self,request):
        return render(request,'user/login.html')

