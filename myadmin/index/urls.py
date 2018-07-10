from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
    url(r'^welcome/$', views.Welcome.as_view()),
    url(r'^resource/$', views.Resource.as_view()),
    url(r'^resourceadd/$', views.ResourceAdd.as_view()),
    url(r'^resourceedit/$', views.ResourceEdit.as_view()),
    url(r'^redirecttest/$', views.ResourceEdit.as_view()),


]