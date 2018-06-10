import sys
from myadmin.myadmin.settings import DATABASES
import pymysql


class User(object):
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



    def getUserInfo(self, userId):
        sql = "SELECT * from user_info WHERE id = %s limit 1 "
        self.__cursor.execute(sql, 1)
        ret = self.__cursor.fetchall()
        self.__cursor.close()
        self.__conn.close()
        return ret


if __name__ == "__main__":
    print(dict(host=DATABASES['default']['HOST'],
               port=DATABASES['default']['PORT'],
               user=DATABASES['default']['USER'],
               passwd=DATABASES['default']['PASSWORD'],
               db=DATABASES['default']['NAME'],
               charset='utf8'))

    user = User()
    ret = user.getUserInfo(1)
    print(ret)
