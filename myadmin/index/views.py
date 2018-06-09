from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

class IndexHandler(View):
    def get(self,request):
        render(request,'index/index.html')

