from utils.BaseModel import MysqlHandler
import json
from utils.common import decimal_serializable, datetime_serializable


class SzStock(MysqlHandler):

    def getList(self, page=1, rows=10):
        start = rows * (page - 1)
        sql = " select * from sz_stock_list limit %s ,%s " % (start, rows)
        ret = self.select(sql)
        return ret

    def getCount(self):
        sql = " select count(*) as n from sz_stock_list"
        count = self.selectCount(sql)
        return count


if __name__ == '__main__':
    SzStock = SzStock()
    res = SzStock.getList(1, 10)
    for index, value in enumerate(res):
        # print(res)
        # print(type(res[0]['stock_date']))
        # print(type(res[0]['general_capital']))
        for k, v in value.items():
            v = decimal_serializable(v)
            value[k] = datetime_serializable(v)
        res[index] = value
    print(json.dumps(res))
