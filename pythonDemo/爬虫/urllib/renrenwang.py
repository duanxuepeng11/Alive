from urllib import request,parse
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
    login_url ="http://www.renren.com/PLogin.do"

    data ={
        "email":"18838189396",
        "password":"d18838189396"
    }
    data = parse.urlencode(data)

    data = request.Request(login_url, data=bytes(data, encoding="utf-8"))

    #发起请求
    response = opener.open(data)

def getHomePage():
    home_url ="http://www.renren.com/964508169/profile"
    response = opener.open(home_url)
    print(response.read().decode("utf-8"))
if __name__ == '__main__':
    login()

    getHomePage()