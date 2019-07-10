import requests
ssion = requests.session()
# 登录
def login():
    # 登录的网站地址
    login_url = "http://www.renren.com/PLogin.do"
    data = {
        "email":"18838189396",
        "password":"d18838189396"
    }
    response = ssion.post(login_url,data=data)
    print(response.content.decode("utf-8"))
    print('-------------------------')
    # 重定向到个人首页
    getHomePage()
# 主页
def getHomePage():
    base_url = "http://www.renren.com/964508169/profile"
    response = ssion.get(base_url)
    print(response.content.decode("utf-8"))
# 主进程
if __name__ == "__main__":
    login()