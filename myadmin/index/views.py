from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
import os, sys
file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, file_path)
from utils.common import require_logined

# Create your views here.

class Index(View):
    @require_logined
    def get(self, request):
        print('index首页中查看的session:%s' % dict(request.session))
        # return HttpResponse('ok')
        return render(request, 'index/index.html')


class Welcome(View):
    def get(self, request):
        return render(request, 'index/welcome.html')






