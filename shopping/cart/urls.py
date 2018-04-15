#Author:Bob
from django.conf.urls import url
from . import views

urlpattern = [
    url(r'cart/$',views.cart.index)
]