from django.conf.urls import url
from . import views  # 注意这是py3的写法  ,如果沿用py2中的写法   import views 启动django服务会报错

urlpatterns = [
    url(r'^$', views.index),
    url(r'^test_update/$', views.test_update),
    url(r'^test_q/$', views.test_q),
    url(r'^shiwu/$', views.shiwu_demo),
    url(r'^shiwu1/$', views.shiwu_demo1),
    url(r'^testaa/$', views.testaa),
    url(r'^sumtest/$', views.sumtest),
    url(r'^map/$', views.map),
]
