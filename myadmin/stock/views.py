from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import HttpResponse


class SzStockList(View):
    def get(self,request):
        render(request,'stock/szlist.html')

