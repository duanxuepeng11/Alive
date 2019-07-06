def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#这样可以求和，但是，我们现在不需要立刻求出来，而是在后面代码中，根据需要再计算

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count2()
print(f1(),f2(),f3())
"""
一个函数可以返回一个计算结果，也可以返回一个函数。
返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
"""




