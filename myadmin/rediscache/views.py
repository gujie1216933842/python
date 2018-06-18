from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.core.cache import cache
import json
from django.shortcuts import HttpResponse

'''
测试把redis当成django项目的缓存

'''
def getCache(self):
    key = 'xiaoming'
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return HttpResponse(data)


def setCache(self):
    cache.set('xiaoming', 'gujie', settings.NEVER_REDIS_TIMEOUT)
    return HttpResponse('ok')
