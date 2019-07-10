#练习使用正则
import re
mm ="c:\\a\\b\\c"
print(mm)
# print(re.match(mm))

pattern = re.compile(r"\d+")

"""
match 方法用于查找字符串的头部（也可以指定起始位置），它是一次匹配，只要找到
了一个匹配的结果就返回，而不是查找所有匹配的结果
"""
m = pattern.match("one12twothree34four")
n = pattern.match("22one12twothree34four")
q = pattern.match("one12twothree34four",3,10)
print(m)
print(n)
print(q)
print(q.group())
print(q.start())
print(q.end())
print(q.span())