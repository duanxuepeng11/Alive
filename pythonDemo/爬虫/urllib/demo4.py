from urllib import request
from urllib import parse

base_url ='http://www.baidu.com/s?'

wd = input("输入搜索关键字")
qs = {
    'wd':wd
}
print(qs) #{'wd': 'aaa'}

qs = parse.urlencode(qs)  #转换url编码
print(qs)  #wd=aaa

#拼接url
fullurl = base_url + qs

response = request.urlopen(fullurl)
html = response.read().decode('utf-8')
print(html)

with open("E:\DXP\爬虫练习\dnf.html",'w',encoding="utf-8") as fp:
    fp.write(html)