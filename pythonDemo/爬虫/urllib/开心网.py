from urllib import parse,request
from http import cookiejar

#定义cookie对象
cookie = cookiejar.CookieJar()
#生成cookie管理器
cookid_handler = request.HTTPCookieProcessor(cookie)
#http请求管理器
http_handler = request.HTTPHandler()
#https请求管理器
https_handler = request.HTTPSHandler()
#发起请求的管理器
opener = request.build_opener(http_handler, https_handler, cookid_handler)
def login():
    login_url ="https://security.kaixin001.com/login/login_post.php"

    data ={
        "loginemail":"18838189396",
        "password":"d18838189396"
    }
    data = parse.urlencode(data)

    #POST
    headers = {
        "Content-Length" : len(data),
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    req = request.Request(login_url, data=bytes(data, encoding="utf-8"),headers=headers)

    #发起请求
    response = opener.open(req)
    # response = request.urlopen(data)
    html = response.read().decode("utf-8")
    # print(html)
    with open("E:\DXP\爬虫练习\kaixin.html",'w',encoding="utf-8") as fp:
        fp.write(html)


def getHomePage():
    base_url ="http://www.kaixin001.com/home/?uid=181866387"
    response = opener.open(base_url)
    html = response.read().decode('utf-8')
    with open("E:\DXP\爬虫练习\kaixin2.html",'w',encoding="utf-8") as fp:
        fp.write(html)

if __name__ == '__main__':
    login()
    getHomePage()