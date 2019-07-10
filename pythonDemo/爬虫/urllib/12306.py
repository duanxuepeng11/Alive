from urllib import  request
import ssl
#忽略 ssl验证
# ssl._create_default_https_context = ssl._create_unverified_context()
response = request.urlopen("https://www.12306.cn/index/")
print(response.read().decode("utf-8"))