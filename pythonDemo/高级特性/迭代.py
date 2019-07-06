d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
        print(key)
        print(d.get(key))
for value in d.values():
    print(value)


for key,value in d.items():
    print(key,value)

for key in d.items():
    print(key)
from collections import Iterable
print(isinstance([1,2,3], Iterable)) # list是否可迭代













