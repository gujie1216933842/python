from django.shortcuts import render, HttpResponse
from django.views.generic.base import View


# Create your views here.

class Index(View):
    def get(self, request):
        request.session['index'] = 'indexvalue'
        print('index首页中查看的session:%s' % dict(request.session))
        # return HttpResponse('ok')
        return render(request, 'index/index.html')


class Welcome(View):
    def get(self, request):
        return render(request, 'index/welcome.html')
