from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from utils.common import require_logined, django_model_opration
from . import models
from django.http import JsonResponse

import datetime
from django.forms.models import model_to_dict


# Create your views here.

class Index(View):
    @require_logined
    def get(self, request):
        print('index首页中查看的session:%s' % dict(request.session))
        username = request.session.get('userInfo').get('username')
        # 获取资源信息
        id = request.GET.get('id', '')
        resource = models.Resource.objects.filter(id=id)

        return render(request, 'index/index.html', {'username': username, 'resource': resource})


class Welcome(View):
    def get(self, request):
        return render(request, 'index/welcome.html')


class Resource(View):
    @require_logined
    def get(self, request):
        return render(request, 'index/resource.html')

    def post(self, request):
        page = request.POST.get('page', 1)
        rows = request.POST.get('rows', 10)
        page = int(page)
        rows = int(rows)
        start = rows * (page - 1)
        end = start + rows - 1
        # 获取数据
        sourceItems = models.Resource.objects.all()[start: end]
        sourceList = django_model_opration(sourceItems)
        count = models.Resource.objects.all().count()
        return JsonResponse({"rows": sourceList, 'total': count})


class ResourceAdd(View):
    def post(self, request):
        name = request.POST.get('name', '')
        link = request.POST.get('link', '')
        category = request.POST.get('category', '')
        # 数据入库
        resourceObj = models.Resource()
        resourceObj.name = name
        resourceObj.link = link
        resourceObj.category = category
        try:
            resourceObj.save()
        except Exception as e:
            return JsonResponse({'code': '01', 'msg': '添加失败'})

        return JsonResponse({'code': '00', 'msg': '添加成功'})


class ResourceEdit(View):
    def post(self, request):
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        link = request.POST.get('link', '')
        category = request.POST.get('category', '')
        raw_update_time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        try:
            models.Resource.objects.filter(id=id).update(name=name, link=link, category=category,
                                                         raw_update_time=raw_update_time)
        except Exception as e:
            return JsonResponse({'code': '01', 'msg': '编辑失败'})

        return JsonResponse({'code': '00', 'msg': '编辑成功'})
