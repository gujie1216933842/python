#Author:Bob

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.goods.as_view()),
    url(r'^detail/$', views.goods.detail),


]