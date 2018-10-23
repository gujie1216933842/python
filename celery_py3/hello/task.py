# rom__future__import absolute_import
from celery import Celery
# 导入redis模块，通过python操作redis
import redis
import django_redis
import pymysql
import simplejson

# 创建celery客户端
# 参数一  指定任务所在的路径，从包名开始制定
# 参数二  指定任务队列（broker），这里使用的reids
app = Celery('tasks', broker='redis://localhost:6379')

app.conf.update(
    #  配置所在时区
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    #  官网推荐消息序列化方式为json
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json', )


@app.task
def inster(tp):
    print("1111111111111111111111111111111111111111111111111")
    # 链接数据库
    db = pymysql.connect(host="localhost", user="root", passwd="mysql", db="insauditdata", charset='utf8')
    cursor = db.cursor()

    # 链接redis池
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    if tp == 1:
        cursor.execute("select rt_bps, avg_bps from t_mem_net_flow order by interface_id")
        results = cursor.fetchall()  # 每查询一条数据返回一个元祖，装入大的元祖中
