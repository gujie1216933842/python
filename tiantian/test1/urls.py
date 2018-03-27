from django.conf.urls import url
from . import views
urlpatterns= [
    url(r'^$',views.index),
    url(r'^index1$',views.index1)
]