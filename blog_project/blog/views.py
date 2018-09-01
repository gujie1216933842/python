from django.shortcuts import render
import logging

# 定义日志器
logger = logging.getLogger('blog.views')


def index(request):
    try:
        f = open('ss.txt', 'r')
    except Exception as e:
        logger.error(e)

    return render(request, 'blog/index.html')
