from pyquery import PyQuery as pq

i = 1
while True:
    doc = pq(url='http://www.tigertrend.net/News/Notice?page={}'.format(i))
    content = doc(".newsCon dl")
    if not content:
        break
    for item in content:
        doc2 = pq(item)
        name = doc2("h3 a").text()
        date = doc2(".date").text()
        site = 'http://www.tigertrend.net{}'.format(doc2("h3 a").attr('href'))
        print(name, date, site)
    i += 1
