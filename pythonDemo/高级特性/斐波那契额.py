def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'

print(fib(6))

def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        yield (b)
        a,b = b,a+b
        n = n+1
    return 'done'


# print(fib2(6).next())
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
print(next(o))
print(next(o))
print(next(o))
# print(next(o))
print("&&&&&&&&&&&&&&&")
print(fib2(6))
print(list(fib2(6)))
for n in fib2(6):
         print(n)

g  = fib2(6)
while True:
    try:
        x = next(g)
        print("g:",x)
    except StopIteration as e:
        print("Generator return values:"+e.value)
        break
