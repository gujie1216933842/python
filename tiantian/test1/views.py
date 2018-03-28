#from django.shortcuts import render
#定义完视图
# Create your views here.
from django.http import *
from django.template import RequestContext,loader
from django.shortcuts import render

def index(request):
    return HttpResponse('hello world')

def index1(request):
    temp = loader.get_template('test1/index.html')
    return HttpResponse(temp.render())


def index2(request):
    return render(request,'test1/index1.html')


def index3(request):
    return render(request,'test1/index1.html')