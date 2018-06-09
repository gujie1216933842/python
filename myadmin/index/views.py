from django.shortcuts import render, HttpResponse
from django.views.generic.base import View


# Create your views here.

class IndexHandler(View):
    def get(self, request):
        return HttpResponse('ok')
        # render(request,'index/index.html')
