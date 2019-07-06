import functools
int2 = functools.partial(int, base=2)
print(int2('100000',base=10))

kw = { 'base': 10 }
print(int('10010', **kw))

max2 = functools.partial(max, 10)
print(max2(1,3,4,5))



