from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'article/^$', views.index),
    url(r'^sqltest/$', views.sqltest)

]
