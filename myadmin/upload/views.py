from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import HttpResponse


# Create your views here.


class UploadExcelUserId(View):
    def get(self, rquest):
        return render(rquest, 'upload/exceluserid.html')

    def post(self, request):
        return HttpResponse('ok')
