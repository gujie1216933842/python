from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'exceluserid/$', views.UploadExcelUserId.as_view()),
    url(r'test/$', views.uploadexcel),

]
