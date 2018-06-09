from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.Index.as_view()),
    url(r'^/welcome$',views.Welcome.as_view()),


]