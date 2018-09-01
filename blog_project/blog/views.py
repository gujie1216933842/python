from django.shortcuts import render
import logging
from django.conf import settings

# 定义日志器
logger = logging.getLogger('blog.views')


# 应用配置文件中的常量
def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            "SITE_DESC": settings.SITE_DESC}


def index(request):
    return render(request, 'blog/index.html')
