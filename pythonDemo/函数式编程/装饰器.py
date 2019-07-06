"""
，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
"""



def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


import functools
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            c = func(*args, **kw)
            print("end")
            return c

        return wrapper
    return decorator

@log2('aaaa')
def now():
    print('2015-3-25')
"""
把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
"""

now()
# print(now.__name__)






