print(abs(-19))

# abs = 10
# print(abs(-19))

# 函数可以作为参数传递
def add(x,y,f):
    return f(x) + f(y)

print(add(-3,5,abs))

def f(x):
    return x*x

r = map(f,[1,2,3,4,5])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,5]))
list1 = [1,2,3,45]
print(sum(list1))

def fn(x,y):
    return x*10 + y

print(reduce(fn,[1,3,5,7,9]))
# print({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['13579'])

def toUpp(str):
    name = str[0].upper()+str[1:].lower()
    return name
L1 = ['adam', 'LISA', 'barTfddFdas']
L2 = list(map(toUpp, L1))
print(L2)

def is_odd(n):
    return n % 2 == 1

filter1 = list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
print(filter1)

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

sorted([36, 5, -12, 9, -21])
sor1 = sorted([36, 5, -12, 9, -21], key=abs)
print(sor1)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
#排序都是默认小——》大顺序排列的
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True) #反向排序
L = [('Aob', 75), ('Adam', 92), ('Bart', 66), ('Esa', 88)]

def mysorted(t):
    print(t[0],"===",t[1])
    return t[0].lower()
    pass
res = sorted(L,key=mysorted)
print(res)
