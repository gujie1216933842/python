from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    list = BookInfo.bookinfo1.filter()
    content = {'list':list}
    print(list)
    return render(request,'booktest/index.html',content)
