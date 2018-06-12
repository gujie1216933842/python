import pymysql
from base import settings

class Base(object):
    _instance = None
    _conn = None
    _cursor = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._conn = pymysql.Connect(
            host=settings.DATABASES['default']['HOST'],
            port=int(settings.DATABASES['default']['PORT']),
            user=settings.DATABASES['default']['USER'],
            passwd=settings.DATABASES['default']['PASSWORD'],
            db=settings.DATABASES['default']['NAME'],
            charset='utf8'
        )
        self._cursor = self._conn.cursor()  # 最终返回数据类型元组
