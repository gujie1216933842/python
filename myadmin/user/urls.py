from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'logout/$',views.Logout.as_view()),
    url(r'login/$',views.Login.as_view()),
    url(r'captcha/$',views.Captcha.as_view()),
    url(r'user_list/$',views.UserList.as_view()),
    url(r'useradd/$',views.UserAdd.as_view()),
    url(r'useredit/$',views.UserEdit.as_view()),
    url(r'userdel/$',views.UserDel.as_view()),
    url(r'test/$',views.Test.as_view()),


]