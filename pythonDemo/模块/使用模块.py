import sys

def test():
    args = sys.argv
    print(args) #路径
    if len(args) ==1:
        print("hello word")
    elif len(args) ==2:
        print("hello.%s!" % args[1])
    else:
        print("too many ...")
"""
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
"""
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__ == '__main__':
    test()
    print(len("aaaa"))
    print(greeting("wzd"))
    print(sys.path)