from django.shortcuts import render
import redis
# Create your views here.


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)  # 建立redis链接池
r = redis.Redis(connection_pool=pool)  # 建立链接
res_range = r.lrange('1', 0, 59)  # 取数据   取60个
str_res = res_range[0]
res = tuple(eval(str_res))
