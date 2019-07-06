
lt1 = list(map(lambda  x:x*x,[1,2,4,5,6]))
print(lt1)
# list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

f=lambda x:x*x
lt2 = list(map(f,[1,2,3,4,5]))
print(lt2)
"""
Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
"""