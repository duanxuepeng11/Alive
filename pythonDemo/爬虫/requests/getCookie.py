import requests

response = requests.get("http://www.baidu.com")
cookieJar = response.cookies
#讲CookieJar转换字典
cookiedict = requests.utils.dict_from_cookiejar(cookieJar)
print(cookiedict)
print(cookieJar)