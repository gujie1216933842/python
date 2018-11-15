from django.shortcuts import render
from .models import User
# Create your views here.
from django.db.models import F

"""F()函数实例"""


def index(request):
    list = User.objects.get(name='aa')
    print(list)
    list.age = F('age') + 1000
    list.save()

    return render(request, 'booktest/index.html')


"""Q()函数实例
作用：对对象进行复杂查询，并支持&（and）,|（or），~（not）操作符。
"""


def test_q(request):
    pass
