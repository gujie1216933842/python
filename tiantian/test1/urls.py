from django.conf.urls import url
from . import views
urlpatterns= [
    url(r'^$',views.index),
    url(r'^index1$',views.index1),
    url(r'^index2$',views.index2),
    url(r'^index3$',views.index3)
]