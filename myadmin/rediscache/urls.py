from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'getcache/$',views.getCache),
    url(r'setcache/$',views.setCache),

    url(r'setsession/$',views.setSession),
    url(r'getsession/$',views.getSession),

]