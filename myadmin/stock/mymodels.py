from utils.BaseModel import MysqlHandler
import json
from utils.common import decimal_serializable, datetime_serializable, my_log


class SzStock(MysqlHandler):

    def getList(self, page=1, rows=10, company_code='', name=''):
        start = rows * (page - 1)
        limit_sql = " limit %s , %s " % (start, rows)
        params = []
        company_code_sql = ''
        if company_code:
            company_code_sql = " and company_code = %s "
            params.append(company_code)
        name_sql = ''
        if name:
            name_sql = " and name = %s "
            params.append(name)

        sql = " select * from sz_stock_list where delete_flag = 0 " + company_code_sql + name_sql + limit_sql
        my_log('sql: %s' % sql, 'stock')
        my_log('params : %s' % params, 'stock')
        ret = self.select(sql, params)
        return ret

    def getCount(self, company_code='', name=''):

        params = []
        company_code_sql = ''
        if company_code:
            company_code_sql = " and company_code = %s "
            params.append(company_code)
        name_sql = ''
        if name:
            name_sql = " and name = %s "
            params.append(name)
        sql = " select count(*) as n from sz_stock_list where delete_flag = 0" + company_code_sql + name_sql
        count = self.selectCount(sql, params)
        return count

    def getGgList(self, page=1, rows=10, stock_code='', stock_name=''):
        start = rows * (page - 1)
        limit_sql = " order by change_date desc  limit %s , %s " % (start, rows)
        params = []
        stock_code_sql = ''
        if stock_code:
            stock_code_sql = " and stock_code = %s "
            params.append(stock_code)
        stock_name_sql = ''
        if stock_name:
            stock_name_sql = " and stock_name = %s "
            params.append(stock_name)

        sql = " select * from sz_senior_stock_change_list where delete_flag = 0 " + stock_code_sql + stock_name_sql + limit_sql
        my_log('sql: %s' % sql, 'stock')
        my_log('params : %s' % params, 'stock')
        ret = self.select(sql, params)
        return ret

    def getGgCount(self, stock_code='', stock_name=''):

        params = []
        stock_code_sql = ''
        if stock_code:
            stock_code_sql = " and stock_code = %s "
            params.append(stock_code)
        stock_name_sql = ''
        if stock_name:
            stock_name_sql = " and stock_name = %s "
            params.append(stock_name)
        sql = " select count(*) as n from sz_senior_stock_change_list where delete_flag = 0" + stock_code_sql + stock_name_sql
        count = self.selectCount(sql, params)
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
