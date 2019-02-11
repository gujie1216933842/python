from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Student
# Create your views here.
from django.db.models import F, Q, Count, Sum
from django.db import connection, transaction, close_old_connections

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


def shiwu_demo(request):
    """
    用装饰器开启事务demo
    :param request:
    :return:
    """
    try:
        package()
    except Exception as e:
        print(e)
    return HttpResponse('ok')


@transaction.atomic
def package():
    # with transaction.atomic:
    User.objects.filter(id=1).update(name='你好yalll')
    Student.objects.filter(ids=5).update(name='ggggg')


"""
with .....   上下文管理器的方式来开启事务
"""


def shiwu_demo1(request):
    e = ''
    try:
        with transaction.atomic():
            User.objects.filter(id=1).update(name='demo1')
            Student.objects.filter(ids=5).update(name='ggggg')
    except Exception as e:
        print(e)

    return HttpResponse('ok')


def testaa(request):
    rows = User.objects.filter(id__in=[1, 2, 3, 4, 5]).values('hobby').annotate(count=Count('*'))
    print(rows)  # 结果  <QuerySet [{'hobby': 'f', 'count': 3}, {'hobby': 'm', 'count': 2}]>
    test_list = []
    for i in rows:
        print('hahahhah:{},count:{}'.format(i['hobby'], i['count']))
        test_list.append('hahahhah:{},count:{}'.format(i['hobby'], i['count']))

    return HttpResponse('ok:{}'.format(test_list))


def sumtest(request):
    """
    django 求和 测试
    :param request:
    :return:
    """
    rows = User.objects.all().values('hobby', 'name').annotate(s=Sum('age'))
    print(rows)  # <QuerySet [{'hobby': 'f', 's': 2419}, {'hobby': 'm', 's': 65}]>

    row_list = []
    row_dict = {}
    for row in rows:
        row_dict[row]
    return HttpResponse('ok')


def map(request):
    return render(request, 'booktest/map.html')


def index_if(request):
    user_list = User.objects.filter(hobby__contains='f').exclude(name__contains='a')
    return render(request, 'booktest/index_if.html', locals())



def group(request):
    return HttpResponse('group')
