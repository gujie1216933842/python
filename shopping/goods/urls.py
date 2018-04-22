#Author:Bob

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.goodsIndex.as_view()),
    url(r'^detail/$', views.goodsDatail.as_view()),


]