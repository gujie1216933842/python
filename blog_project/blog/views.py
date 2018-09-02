from django.shortcuts import render
import logging
from django.conf import settings
from .models import *

# 引入django原生的分页类
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

# 定义日志器
logger = logging.getLogger('blog.views')


# 应用配置文件中的常量
def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            "SITE_DESC": settings.SITE_DESC}


def index(request):
    category = None
    article_list = None
    try:
        # 分类信息获取(导航数据)
        category = Category.objects.all()
        # 广告信息
        # 最新文章数据(涉及到分页,过滤器的使用)

        article_list = Article.objects.all()
        paginator = Paginator(article_list, 10)

        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
            logger.info(article_list)
        except (InvalidPage, EmptyPage, PageNotAnInteger):
            article_list = paginator.page(1)

        # 文章归档
        # 1.先要去获取到文章中有的 年份-月份 2015-06 文章归档
        # 自定义manager管理器
        archive_list = Article.objects.distinct_date()

    except Exception as e:
        logger.error(e)

    return render(request, 'blog/index.html', locals())


def archive(request):
    try:
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)

        # Article对象做模糊查询
        article_list = Article.objects.filter(date_publish__contains=year + '-' + month)
        paginator = Paginator(article_list, 2)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
            logger.info(article_list)
        except (InvalidPage, EmptyPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)

    return render(request, 'blog/archive.html', locals())  # locals()返回一个包含当前作用域里面的所有变量和它们的值的字典。


from django.db import connection


def sqltest(request):
    '''
    :desc django中执行原生sql语句
          django中有两个方法
          1.raw()
          2.execute()
          注意:django官方,并不推荐此类方法,非必要的时候尽量不要使用,因为:数据库的迁移会有影响
    '''
    # 以获取文章信息为例
    # raw() 方法 ,注意,raw()方法是用select 字段中一定要含有主键,即id字段
    list1 = Article.objects.raw('select id,title from blog_article where id = %s', (1))
    for item in list1:
        print(item)

    # execute()方法
    cursor = connection.cursor()
    cursor.execute('select id,title from blog_article where id = %s', (1))

    list2 = cursor.fetchall()
    for item2 in list2:
        print(item2)
