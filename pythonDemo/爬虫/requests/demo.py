import requests

response = requests.get("http://www.langlang2017.com")
response = requests.request("get","http://www.langlang2017.com")

kw = {'kw':"长城"}
headers ={
    "User-Agent":"Mozilla/5.0 (xxxxx"
}
print(response)

response = requests.get("xxxx",params=kw,headers=headers)
#查看相应内容 ,返回的是unicode格式的数据
print(response.text)
#查看响应内容,返回的是字符流数据
print(response.content)
print(response.url)

print(response.encoding)
print(response.status_code)

"""
使用 response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大
多数 Unicode 字符集都能被无缝地解码。
使用 response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保
存图片等二进制文件。
"""

#post请求
data = {

}
response = requests.post("http://www.baidu.com", data=data)

#代理(proxies参数)
proxies={
    "http":"xxxx1",
    "https":"xxxxx2"
}
requests.request("get","xxxx",proxies=proxies)




