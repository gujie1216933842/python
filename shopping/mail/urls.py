#Author:Bob

from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.goodsIndex.as_view()),  #as_view()括号一定要加上
    url(r'^send/$', views.sendHandler.as_view()),
    #url(r'^send/$', views.send),


]