"""
上一个例子返回的没有http报头等信息,如果想要必须用Request来调用URL
"""
from urllib import request
base_url = "http://www.langlang2017.com"

req = request.Request(base_url)

#发起请求
response = request.urlopen(req)

html = response.read().decode('utf-8')

with open("E:\DXP\爬虫练习\langlang.html",'w',encoding="utf-8") as fp:
    fp.write(html)
