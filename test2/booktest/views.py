from django.shortcuts import render
from .models import User
# Create your views here.
from django.db.models import F
def index(request):

    list = User.objects.get(name='aa')
    print(list)
    list.age = F('age')+ 1000
    list.save()

    return render(request,'booktest/index.html')
