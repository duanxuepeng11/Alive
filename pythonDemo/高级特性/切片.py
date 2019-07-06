L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


print(L[0:3])   #['Michael', 'Sarah', 'Tracy']
print(L[:3])    #['Michael', 'Sarah', 'Tracy']

print(L[1:3])   #['Sarah', 'Tracy']
print(L[1:])    #[ 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[-1])    #['Jack']

print(L[-2:])   #'Bob', 'Jack'

print(L[-2:-1])  #Bob', 'Jack'

L2 = list(range(100))
print(L2[:10:2])        #0246
#所有数，每5个取一个：
print(L2[::5])           #051015


print((0, 1, 2, 3, 4, 5)[:3])   #012

print('ABCDEFG'[:3]) #ABC











