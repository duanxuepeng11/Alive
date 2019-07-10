from urllib import request,parse
import os

"""
        http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0
第二页： http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=50
第三页： http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=100
"""

def tieba(kw,start,end):
    dir_name = 'E://DXP//爬虫练习//tieba//' + kw + '//'
    if not os.path.exists(dir_name): #不存在就创立
        os.makedirs(dir_name)
    qs = {
        'kw':kw,
    }
    #关系
    #1 0
    #2 50
    #3 100

    # for i in range(int(start,int(end) +1)):
    for i in range(int(start),int(end)):
       print(i)
       pn  = (i -1)*50
       qs['pn'] = str(pn)
       print("qs %s " % qs)
       qs_data = parse.urlencode(qs)

       fullurl =base_url + qs_data

       print("downlong page %s" % fullurl)
       response = request.urlopen(fullurl)
       with open(dir_name+str(i)+".html",'w',encoding="utf-8") as fp:
            html = response.read().decode("utf-8")
            fp.write(html)

if __name__ == '__main__':
    base_url ='https://tieba.baidu.com/f?'
    kw = input('贴吧名称')
    start = input("起始页:")
    end = input("结束页:")
    tieba(kw,start,end)