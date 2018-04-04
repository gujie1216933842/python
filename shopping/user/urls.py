#Author:Bob
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/$',views.user.login),
    url(r'regiser/$',views.user.register)



]