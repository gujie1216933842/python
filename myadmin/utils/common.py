# Author:Bob
''''
装饰器
'''
import functools
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.http import HttpResponseRedirect



#如果登录则转到登录页面
def require_logined(func):
    def login_fun(obj,request,*args,**kwargs):
        if request.session.get('userInfo'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url',request.get_full_path)
            return red
    return login_fun






def django_model_opration(Items):
    new_list = []
    for item in Items:
        new_item = model_to_dict(item)
        if hasattr(item, 'raw_add_time'):
            new_item['raw_add_time'] = item.raw_add_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            new_item['raw_add_time'] = ""

        if hasattr(item, 'raw_update_time'):
            new_item['raw_update_time'] = item.raw_update_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            new_item['raw_update_time'] = ""
        new_list.append(new_item)
    return new_list
