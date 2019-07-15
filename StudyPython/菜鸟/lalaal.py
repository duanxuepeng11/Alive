from collections import deque

# 这是单行注释
print("hello, world!!!")
'''
这是多行注释
啦啦啦....
pass 没什么用处,空语句,完全是为了好看结构工整..
'''
def a():
    '''这是文档字符串'''
    pass

print(a.__doc__)

a = 21
b = 10
c = a+b
print(c)
c +=a
c /=a
print(c)

# py集合
list = [1,2,3,4,5]
l1 = 1
if (l1 in list):
    print("变量a在集合list中")
else:
    print("error")

# python身份运算符
d = 20
e = 20
f = e
print(d is e)
print(id(f) is id(e))
print(d is not e)
print(d == e)
print(d == f)
print(e == f)

x=100
y = float(x) #将x转换为float

#字符串
var1 = "Hello world!~"
var2 = "Runoob"
print(var1[1])
print(var2[1:5])  #前包后不报  unoo
print(var2[:5])   #从头开始.获取5个 Runoo

# 格式化字符串

print("我叫%s 今年%d岁" % ('小码',10))

pstr ='''aaa
addd(\t)
fff
gggg'''
print(pstr)
pstr2 ="""qqqq
eeee(\t)
rrrr[\n]
tttt"""
print(pstr2)

# python 列表
list0 = ['google',"Runoob",1005,1998]
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
print(list0[1])
print(list1[1])
print(list2[2])
print(list3[1])
#更新列表
list1[3] = 2001
print(list1[3])
#删除列表
del list1[2]
print("删除第三个元素",list1)
#列表截取
L=['Google', 'Runoob', 'Taobao']
print(L[2])
print(L[-2])
print(L[1:])
#元组
tup1 =('Google','Runoob',1995,2003)
for x in tup1:
    print(x)

#字典操作
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键 'Name'
#dict.clear()     # 清空字典
#del dict         # 删除字典

print ("dict['Age']: ", dict['Age'])
#print ("dict['School']: ", dict['School'])

for i in range(0,10,3):
    print(i)

#定义函数
def hello():
    print("hello world!!!!!")

def area(width,height):
    return width+height


#队列使用
queue = deque(["Eric",'John',"Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
# queue.pop(0)
print(queue)
#python3导包
import sys
print('命令行参数如下')
for i in sys.argv:
    print(i)

print("\n\n\nPython 路径为:",sys.path,'\n')

'''
from ....import
把from指向的模块中的一个指定的部分导入到当前命名空间中

from .... import *
把一个模块的所有内容导入到当前模块中
'''
#读取键盘输入
str = input("请输入:")
print("你输入的内容是: "+str)
#异常
while True:
    try:
        x = int(input("please enter a number :  "))
        break
    except ValueError:
        print("error")