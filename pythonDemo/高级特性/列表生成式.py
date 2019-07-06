list1 = list(range(1,11))
print(list1)

list2 = [x * x for x in range(1, 11)]
print(list2)
list3 = [x * x for x in range(1,11) if x%2==0]
print(list3)

list4 = [m + n for m in 'abc' for n in  'xyz']
print(list4)
import os #导入os模块，
list5 = [d for d in os.listdir('.')]
print(list5)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
list6 = [k +'=' +v for k,v in d.items()]
print(list6)


L = ['Hello', 'World', 18, 'Apple', None]
list7 = []
for s in L:
    if(isinstance(s,str)==False):
        list7.append(s)
    else:
        list7.append(s.lower())
print(list7)