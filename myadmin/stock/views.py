from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from . import mymodels
from utils.common import decimal_serializable, datetime_serializable


class SzStockList(View):
    def get(self, request):
        return render(request, 'stock/szlist.html')

    def post(self, request):
        page = request.POST.get('page', 1)
        rows = request.POST.get('rows', 10)
        SzStockList = mymodels.SzStock()
        ret = SzStockList.getList(int(page), int(rows))
        total = SzStockList.getCount()['n']
        for index, value in enumerate(ret):
            for k, v in value.items():
                v = decimal_serializable(v)
                value[k] = datetime_serializable(v)
            ret[index] = value

        return JsonResponse({'rows': ret, 'total': total})