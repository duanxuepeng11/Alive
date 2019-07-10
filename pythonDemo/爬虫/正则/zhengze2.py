import re
# pattern = re.compile(r'([a-z]+) ([a-z])+',re.I) #re.I 表示忽略大小写
pattern = re.compile(r'([a-zA-Z]+) ([a-zA-Z])+') #re.I 表示忽略大小写
m = pattern.match("helloWorlD Hi jjava Ppy")
print(m) #如果匹配成功返回一个match对象
# print(m.group())
# print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())
print(m.span())
print(m.span(0))
print(m.span(1))
print(m.span(2))
print(m.start())
print(m.end())
print(m.end())

"""
match 方法 从头匹配,匹配到了就停止了,头如果不匹配则返回没有
search方法 从头开始匹配,头匹配不上还会往后继续匹配,其他都跟match一样
findall方法 上面2个都是匹配一个,而这个方法匹配多个值
finditer方法  他跟上一个一样,唯一不同的是返回的是一个迭代器,而之前上面的
3个方法返回的都是Match,然后通过遍历可以获取值(start,end,span,group...等)
split方法 按照指定规则对字符串进行切分
sub
"""
pattern2 = re.compile(r"\d+")
result1 = pattern2.findall("hello 1234 444")
print(result1)

p = re.compile(r'[\s\,\;]+')
print(p.split("a,b;; c    d"))

p2 = re.compile(r"(\w+) (\w+)") #\w = [A-Za-z0-9]
s = 'hello 123, hello 456'
print(p2.sub(r"hello aaa",s)) #使用hello world 替换hello 123
print(p2.sub(r'\2 \1',s))

def func(m):
    return "h1" + " " + m.gropu(2)

print(p2.sub(func,s))
print(p2.sub(func,s,1))

#中文 [u4e00-u9fa5]
title = u'你好,hello,世界'
# re.compile(ur'[\u4e00-\u9fa5]')
#py 3.6不支持ur开头