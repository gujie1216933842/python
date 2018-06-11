from myadmin.base import mode1

class User(mode1.Base):

    def getUserInfo(self, userId):
        sql = "SELECT * from user_info WHERE id = %s limit 1 "
        self._cursor.execute(sql, 1)
        ret = self._cursor.fetchall()
        self._cursor.close()
        self._conn.close()
        return ret


if __name__ == "__main__":
    user = User()
    ret = user.getUserInfo(1)
    print(ret)
