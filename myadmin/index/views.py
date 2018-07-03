from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from utils.common import require_logined


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
    def get(self, request):
        return render(request, 'index/source.html')
