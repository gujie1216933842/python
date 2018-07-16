import pymysql.cursors


class MysqlHandler:
    # 获取数据库连接
    def getConn(self):
        try:
            conn = pymysql.connect(host='47.97.165.75',
                                   port=3306,
                                   user='root',
                                   passwd='123',
                                   db='stock',
                                   charset='utf8')
            return conn
        except Exception as e:
            print("getConn Error:%s" % e)

    def select(self, sql, *args):
        connect = self.getConn()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)  # 返回结果为字典
        try:
            cursor.execute(sql, list(args))
            ret = cursor.fetchall()
            return ret
        except Exception as e:
            print("select Error:%s" % e)
        finally:
            cursor.close()
            connect.close()

    def selectCount(self, sql, *args):
        connect = self.getConn()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)  # 返回结果为字典
        try:
            cursor.execute(sql, list(args))
            ret = cursor.fetchone()
            return ret
        except Exception as e:
            print("selectCount Error:%s" % e)
        finally:
            cursor.close()
            connect.close()

    # 带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
    def update(self, sql, params):
        connect = self.getConn()
        cursor = connect.cursor()  # 最终返回数据类型元组
        try:
            count = cursor.execute(sql, params)
            connect.commit()
            return count
        except Exception as e:
            connect.rollback()
            print("update Error:%s" % e)
        finally:
            cursor.close()
            connect.close()


if __name__ == "__main__":
    db = MysqlHandler()


    def get():
        sql = "select count(*) as n from sz_stock_list"
        ret = db.selectCount(sql)
        print(ret)


    get()


    def update():
        pass


    def insert():
        pass


    def delop():
        pass
