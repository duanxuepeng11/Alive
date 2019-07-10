"""
使用代理 IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。
很多网站会检测某一段时间某个 IP 的访问次数(通过流量统计，系统日志等)，如果访
问次数多的不像正常人，它会禁止这个 IP 的访问。所以我们可以设置一些代理服务器，每
隔一段时间换一个代理，就算 IP 被禁止，依然可以换个 IP 继续爬取。
request 中通过 ProxyHandler 来设置使用代理服务器，下面代码说明如何使用自定义
opener 来使用代理：


"""
from urllib import request,parse

#使用代理
httpproxy_handler = request.ProxyHandler({"http": "139.223.312.22:80"})

#无代理
nullproxy_handle = request.ProxyHandler({})

#定义开关
proxySwitch = True

if proxySwitch:
    opener = request.build_opener(httpproxy_handler)
else:
    opener = request.build_opener(nullproxy_handle)

req = request.Request("http://www.baiud.com")
response = opener.open(req)
print(response.read())