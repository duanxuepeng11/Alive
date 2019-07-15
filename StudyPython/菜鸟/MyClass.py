class MyClasss:
    """这是一个简单的类"""
    i = 123456
    def f(self):
        return "hello world"
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = MyClasss(3,4)
print(x.i)
print(x.f())
print(x.i)
print(x.r)

class Test:
    def prt(self):
        print(self)
        print(self.__class__)   #class是获取类的实例,而非类


t = Test()
t.prt()

class people:
    #定义基本属性
    name =''
    age = 0
    #定义私有属性 ,私有属性外部无法直接访问
    __weight=0
    #构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age = a
        self.__weight=w
    #定义方法
    def speak(self):
        print("%s 说: 我%d岁." %(self.name,self.age))

#实例化类
# p = people('runoob',10,30)
# p.speak()

#单继承
class student(people):
    grade =''
    def __init__(self,n,a,w,g):
        #调用父类的构造
        people.__init__(self,n,a,w)
        people.speak(self)
        self.grade = g
    #覆写父类的方法:
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

# s = student('ken',10,50,5)
# s.speak()

#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#多重继承
class sample(student,speaker):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

    #私有属性和方法
    __siyou =3
    def __siyou2(self):
        print("这是私有方法")

test = sample('tim',23,70,3,'py')
test.speak()

#运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
print(v1)
import os
print(os.getcwd())
from datetime import date
now = date.today()
print(now)