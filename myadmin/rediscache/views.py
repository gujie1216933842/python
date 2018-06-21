from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.core.cache import cache
import json
from django.shortcuts import HttpResponse

'''
测试把redis当成django项目的缓存

'''
def getCache(request):
    key = 'xiaoming'
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return HttpResponse(data)


def setCache(request):
    cache.set('xiaoming', 'gujie', settings.NEVER_REDIS_TIMEOUT)
    return HttpResponse('ok')



def setSession(request):
    request.session['username'] = 'Django'
    request.session['verify_code'] = '123456'
    return HttpResponse('保存session数据成功')

def getSession(request):
  """获取session数据"""
  username = request.session.get('username')
  verify_code = request.session.get('verify_code')
  text = 'username=%s, verify_code=%s' % (username, verify_code)
  return HttpResponse(text)