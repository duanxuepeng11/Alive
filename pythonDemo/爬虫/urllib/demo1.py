from urllib import request
#定义一个响应对象
response= request.urlopen(url="https://www.dahe.cn/")

#读取页码信息
content = response.read()  ####返回对象

#转码
html = content.decode("utf-8")

#保存
with open('E:\DXP\爬虫练习\dahe.html',"w",encoding="utf-8") as fp:
    fp.write(html)
