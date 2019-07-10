"""
模拟用户的真实访问行为,
添加headers头

"""
from urllib import request
from random import random
base_url = "http://www.langlang2017.com"

headers ={
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

header_list ={
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

#在Request中假如Header,来构造一个完整的HTTP请求消息
req = request.Request(base_url,headers=headers)
# req = request.Request(base_url)
#req.add_header("User-Agent",random.choice(header_list))  2中给req添加header的User-Agent方式
req.add_header("Connection","keep-alive")
c = req.get_header(header_name="Connection")
d = req.get_header(header_name="User-Agent")
print(c)
print(d)


#发起请求
response = request.urlopen(req)

html = response.read().decode('utf-8')

with open("E:\DXP\爬虫练习\langlang.html",'w',encoding="utf-8") as fp:
    fp.write(html)
