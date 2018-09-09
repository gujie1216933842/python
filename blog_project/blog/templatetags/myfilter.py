# -*-coding: utf-8 -*-
from django import template

register = template.Library()


# 定义一个将日期中的阿拉伯数字转化为中文的过滤器
# @register.filter  # 另一种注册的方式
def month_to_upper(key):
    return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'][key.month - 1]


# 注册过滤器
register.filter('month_to_upper', month_to_upper)
