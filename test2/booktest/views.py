from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    list = BookInfo.bookinfo1.filter(heroinfo__hcontent__contains='八')
    content = {'list':list}
    return render(request,'booktest/index.html',content)
