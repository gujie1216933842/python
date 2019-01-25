from pyquery import PyQuery as pq

doc = pq(url='http://www.rtfund.com/main/fund/index.shtml')
content = doc('.jj_index_table04')
name_list = []
for item in content:
    for it in item:
        doc1 = pq(it)
        name = doc1('td').eq(1).text()
        if name not in name_list:
            name_list.append(name)
        else:
            continue
        code = doc1('td').eq(2).text()
        net_value_date = doc1('td').eq(3).text()  # 净值日期
        net_asset_value = doc1('td').eq(4).text()  # 单位净值
        print(name, code, net_value_date, net_asset_value)
