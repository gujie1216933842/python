from django.shortcuts import render,HttpResponse
from django.views.generic.base import View
# Create your views here.

class IndexHandler(View):
    def get(self,request):
        HttpResponse('ok')
        #render(request,'index/index.html')

