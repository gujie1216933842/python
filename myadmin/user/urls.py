from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'logout/$',views.Logout.as_view()),
    url(r'login/$',views.Login.as_view()),
    url(r'captcha/$',views.Captcha.as_view())


]