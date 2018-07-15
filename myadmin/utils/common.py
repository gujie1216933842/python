# Author:Bob
''''
装饰器
'''
import functools
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

import os, time, datetime, decimal


# 如果登录则转到登录页面
def require_logined(func):
    def login_fun(obj, request, *args, **kwargs):
        try:
            if request.session['userInfo']:
                return func(obj, request, *args, **kwargs)
            else:
                red = HttpResponseRedirect('/user/login')
                # red.set_cookie('url',request.get_full_path)
                return red
        except Exception as e:
            red = HttpResponseRedirect('/user/login')
            # red.set_cookie('url',request.get_full_path)
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


def datetime_serializable(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return obj


def decimal_serializable(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    else:
        return obj


def my_log(content, logName):
    '''
    :param content:   文件内容
    :param logName:   日志名
    :return:
    '''
    # 判断是否存在脚本的兄弟层级中是否存在log文件
    now_year = time.strftime('%Y', time.localtime())
    now_mouth = time.strftime('%m', time.localtime())
    now_day = time.strftime('%d', time.localtime())
    log_path = "%s/logs/%s/%s/%s/" % (os.path.dirname(os.path.dirname(__file__)), now_year, now_mouth, now_day)
    try:
        if not os.path.exists(log_path):
            os.makedirs(log_path)  # 创建文件夹
    except Exception as e:
        print('创建文件异常1:%s' % e)

    log_file_path = "%s/%s.log" % (log_path, logName)
    log_file_handle = open(log_file_path, 'a')

    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    log_content = "[%s]: %s" % (now_time, content)

    log_file_handle.write(log_content)
    log_file_handle.write('\n')

    log_file_handle.close()
