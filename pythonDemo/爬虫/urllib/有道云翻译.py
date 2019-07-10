from urllib import request,parse
import time
import random
import hashlib
import json


def getMD5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value,encoding="utf-8"))
    # print("md5 %s" % md5)
    sign = md5.hexdigest()
    # print(sign)
    return sign

def ydfanyi(key):

    base_url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = int(time.time()*1000 + random.randint(0,10))
    sign = 'fanyideskweb' + key + str(salt) + "rYOD~O'nMO}g5Mmlz%lG4"
    sign = getMD5(sign)
    data={
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        # "salt":salt ,
        # "sign": sign,
        "salt": "15627425384678",
        "sign": "5e1966f860ba5565fef3185f784ef79c",
        "ts": "1562740071510",
        "bv": "9ef61dc3d2f65f61d71a16bd47c6e9ee",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    data = parse.urlencode(data)
    headers ={
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate", 不要压缩
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": 'OUTFOX_SEARCH_USER_ID_NCOO=1778706620.5220265; OUTFOX_SEARCH_USER_ID="1342920754@10.169.0.84"; _ga=GA1.2.1404069714.1544185200; P_INFO=duanxuepengg@163.com|1552269759|0|other|00&99|zhj&1552262497&mail_client#hub&420100#10#0#0|&0|unireg|duanxuepengg@163.com; _ntes_nnid=b9e660d220313f3b744acf633a645558,1553236533290; JSESSIONID=abcefRD9D39gOcccAmwVw; ___rl__test__cookies=1562740071503',
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(base_url, data=bytes(data, encoding="utf-8"), headers=headers)

    response = request.urlopen(req)

    # print(response.read().decode("utf-8"))
    """
    {"translateResult":[[{"tgt":"aaa","src":"aaa"}]],"errorCode":0,"type":"en2zh-CHS",\
    "smartResult":{"entries":["","abbr. 美国汽车协会（American Automobile Association）；\
    美国仲裁协会（American Arbitration Association）；美国广告学会（American Academy of Advertising）；
    业余体育协会（Amateur Athletic Association）；美国人类学协会（American Anthropological Association）\r\n"],"type":1}}
    """
    data_json = response.read().decode("utf-8")
    data = json.loads(data_json)
    #print(data)
    res = ''
    for item in data['translateResult']:
        res += item[0]['tgt']
    print(data['smartResult'])
    data2 = data['smartResult']
    print(data2['entries'])
    for strs in data2['entries']:
        print("111")
        print(strs)


if __name__ == '__main__':
    key = input("输入你要翻译的单词:")
    ydfanyi(key=key)