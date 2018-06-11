from myadmin.myadmin.settings import DATABASES
import pymysql


class Base(object):
    _instance = None
    __conn = None
    __cursor = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.__conn = pymysql.Connect(
            host=DATABASES['default']['HOST'],
            port=int(DATABASES['default']['PORT']),
            user=DATABASES['default']['USER'],
            passwd=DATABASES['default']['PASSWORD'],
            db=DATABASES['default']['NAME'],
            charset='utf8'
        )
        self.__cursor = self.__conn.cursor()  # 最终返回数据类型元组
