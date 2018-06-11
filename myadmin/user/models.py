import sys,os
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'base/')
print(file_path)
sys.path.insert(0,file_path)

from myadmin.base import mode1

class User(mode1.Base):

    def getUserInfo(self, userId):
        sql = "SELECT * from user_info WHERE id = %s limit 1 "
        self._cursor.execute(sql, 1)
        ret = self._cursor.fetchall()
        self._cursor.close()
        self._conn.close()
        return ret


    def userLogin(self,username,password):
        sql = " select * from user_info where username = %s and password = %s "
        self._cursor.execute(sql,(username,password))
        ret = self._cursor.fetchall()
        return ret


if __name__ == "__main__":
    user = User()
    ret = user.getUserInfo(1)
    print(ret)