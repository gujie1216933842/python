from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'szlist/$', views.SzStockList.as_view()),
    url(r'szchangelist/$', views.SzGgChangeStockList.as_view()),

]
