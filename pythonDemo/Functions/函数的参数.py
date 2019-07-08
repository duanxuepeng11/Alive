# """
# 位置参数
# """
# def powder(x):
#     return x * x
#
# """
# 默认参数
# """
#
# def power(x,n=2):
#     s = 1
#     while n >0:
#         n = n- 1
#         s = s * s
#     return s
# """
# 可变参数
# """
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc([1, 2, 3])) #需要传入一个list或则tuple
#
# #上面2者一样结果
# def calc2(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc2(1, 2, 3))
#
# """
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个
# 含参数名的参数，（注意注意，这里时区别？？？啥是参数名参数)
# 这些关键字参数在函数内部自动组装为一个dict。请看示例：
# """
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# p1 = person('Bob', 35, city='Beijing')
# p1
# p2 = person('Adam', 45, gender='M', job='Engineer')
# p2
# """
# 命名关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)
# 调用时候*后面必须使用key:value形式
# 如下：
#  person('Jack', 24, city='Beijing', job='Engineer')
# """
#
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
#
# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)
#
# args2 = (1, 2, 3)
# kw2 = {'d': 88, 'x': '#'}
# f2(*args2, **kw2)