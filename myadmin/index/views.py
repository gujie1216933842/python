from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from utils.common import require_logined, django_model_opration
from . import models
from django.http import JsonResponse


# Create your views here.

class Index(View):
    @require_logined
    def get(self, request):
        print('index首页中查看的session:%s' % dict(request.session))
        username = request.session.get('userInfo').get('username')
        # return HttpResponse('ok')
        return render(request, 'index/index.html', {'username': username})


class Welcome(View):
    def get(self, request):
        return render(request, 'index/welcome.html')


class Source(View):
    @require_logined
    def get(self, request):
        return render(request, 'index/source.html')

    def post(self, request):
        page = request.GET.get('page', 1)
        rows = request.GET.get('rows', 10)
        page = int(page)
        rows = int(rows)
        start = rows * (page - 1)
        end = start + rows - 1
        # 获取数据
        sourceItems = models.Resource.objects.all()[start, end]
        sourceList = django_model_opration(sourceItems)
        count = models.Resource.objects.all().count()
        return JsonResponse({"rows": sourceList, 'total': count})
