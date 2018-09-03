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
https://blog.csdn.net/oolawokao/article/details/77994527

nginx + uwsgi + django 原理:
https://www.linuxidc.com/Linux/2017-03/141785.htm
'''