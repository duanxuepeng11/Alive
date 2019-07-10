import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def __init__(self,p):
        self.p = p

    def start_element(self,name,attrs):
        if name !="map":
            name = attrs['title']
            number = attrs['href']
            self.p.append((name,number))

    def end_element(self,name):
        pass

    def char_data(self,text):
        pass

def get_p(url):
    p =[]
    # 1 根据url获取网页信息
    content = requests.get(url).content.decode('gb2312')
    start = content.find('<map name=\"map_86\" id=\"map_86\">')
    end = content.find('</map>')
    content = content[start:end+len('</map>')].strip()
    print(content)
    # 2 、解析
    handler = DefaultSaxHandler(p)
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(content)
    return p
p = get_p('http://ip138.com/post/')
print(p)