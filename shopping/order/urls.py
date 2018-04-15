# Author:Bob
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'user_center_order/$', views.order.index),
    url(r'user_center_site/$', views.order.address)
]
