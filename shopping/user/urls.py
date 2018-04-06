# Author:Bob
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/$', views.user.login),
    url(r'register/$', views.user.register),
    url(r'register_handler/$', views.user.register_handler),
    url(r'register_exist/$', views.user.register_exist),
    url(r'login_handler/$', views.user.login_handler)

]
