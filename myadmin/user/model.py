from myadmin.myadmin.settings import DATABASES
import pymysql
from myadmin.base import mode1


class User(mode1.Base):

    def getUserInfo(self, userId):
        sql = "SELECT * from user_info WHERE id = %s limit 1 "
        self.__cursor.execute(sql, 1)
        ret = self.__cursor.fetchall()
        self.__cursor.close()
        self.__conn.close()
        return ret


if __name__ == "__main__":
    user = User()
    ret = user.getUserInfo(1)
    print(ret)
