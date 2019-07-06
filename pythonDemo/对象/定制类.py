class Student(object):
    def __init__(self,name):
        self.name = name
    #美化输出形式的
    def __str__(self):
        return 'student object name is %s' % self.name
    def __call__(self, *args, **kwargs):
        print("aaaaaaaaaaa")
s1 = Student("Michael")
print(s1)
s1()
# print(s1.name)

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a >100000:
            raise StopIteration
        return self.a
    def __getitem__(self, item):
        a,b = 1,1
        print("item,%s" % item)
        for x in range(item):
            print("aaa %s," % a)
            a,b=b,a+b
        return a
    def __getattr__(self, item):
        #没有找到属性时 默认掉这个
        pass
    def __call__(self, *args, **kwargs):
        print("aaaaaaaaaaa")
# for n in Fib():
#     print(n)
print(Fib()[5])

for x in range(5):
    print(x)

Fib()