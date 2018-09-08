# test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
    #return ["Hello World"] # python2


'''
pip install uwsgi

uwsgi --http :9000 --wsgi-file uwsgi_test.py
启动uwsgi服务器后,在浏览器中输入地址  http//:47.97.165.75:9000
如果服务正常   ,页面返回   Hello World

'''
'''


2)验证uwsgi：

    进入到和django项目的manage.py所在的文件夹，运行如下命令：
        uwsgi --http :8000 --module Sport.wsgi


https://blog.csdn.net/oolawokao/article/details/77994527

nginx + uwsgi + django 原理:
https://www.linuxidc.com/Linux/2017-03/141785.htm


uwsgi 启动django项目
uwsgi --ini uwsgi.ini


重启uwsgi进程
首先在uwsgi.ini配置文件中增加
stats=%(chdir)/uwsgi.status
pidfile=%(chdir)/uwsgi.pid

然后执行以下  uwsgi --ini uwsgi.ini  才会生成  uwsgi.status  /  uwsgi.pid  这两个文件

查看命令   cat  uwsgi.pid  这里要注意文件目录路径,要对应上
uwsgi --reload uwsgi.pid 





'''