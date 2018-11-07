from django.shortcuts import render
from .models import User
# Create your views here.

def index(request):
    list = User.objects.all()
    content = {'list':list}
    print(list)
    return render(request,'booktest/index.html',content)
