from django.conf.urls import url
from . import views  #注意这是py3的写法  ,如果沿用py2中的写法   import views 启动django服务会报错

urlpatterns = [
    url(r'^$', views.index),
]