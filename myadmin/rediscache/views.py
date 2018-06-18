from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.core.cache import cache
import json

def getCache(self):
    key = 'gujie'
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data


def setCache(self):
    cache.set('xiaoming','gujie',settings.NEVER_REDIS_TIMEOUT)

