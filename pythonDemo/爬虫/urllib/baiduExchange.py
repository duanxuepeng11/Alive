from urllib import request,parse
import json

base_url = 'http://fanyi.baidu.com/sug'

def fanyi(kw):
    data = {
        'kw':kw
    }
    data = parse.urlencode(data)
    length = len(data)
    #构造请求头

    headers = {
        'Content-Length':length
    }

    #构造请求对象
    req = request.Request(url=base_url, data=bytes(data, encoding='utf-8'), headers=headers)

    response = request.urlopen(req)
    json_data = response.read().decode("utf-8")

    print(json_data)
    #转换字典
    json_data = json.loads(json_data)
    print(json_data)

    #整理输出
    res = ''
    for item in json_data['data']:
        res += item['v'] + '\n'
    print(res)

if __name__ == '__main__':
    while True:
        kw = input("请输入翻译的单词")
        if kw =='q':
            break
        fanyi(kw)