from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
from django.db.models import F, Q

"""F()函数实例"""


def index(request):
    list = User.objects.get(name='aa')
    print(list)
    list.age = F('age') + 1000
    list.save()

    return render(request, 'booktest/index.html')


"""Q()函数实例
作用：对对象进行复杂查询，并支持&（and）,|（or），~（not）操作符。
filter()方法中查询都是以and查询的,如果要使用复杂的sql查询,比如or,not 需要用到Q函数


"""


def test_q(request):
    rows = User.objects.filter(hobby__startswith='f')
    for row in rows:
        print(row.id)

    rows = User.objects.filter(~Q(age=32) & ~Q(age=33))
    for row in rows:
        print('{}---{}---{}'.format(row.id, row.name, row.age))

    return HttpResponse('ok')


def test_update(request):
    row_count = User.objects.filter(id=3).update(hobby='大名')
    print(row_count)
    return HttpResponse('ok')
