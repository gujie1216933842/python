from django.shortcuts import render
from django.views.generic import View


# Create your views here.


class UploadExcelUserId(View):
    def get(self, rquest):
        return render(rquest, 'upload/exceluserid.html')
