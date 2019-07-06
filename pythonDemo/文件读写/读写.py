
try:
    f = open("///////////","r")
    a = f.read()
    print(a)
except Exception as e:
    print("发下面哟从激昂:",e)
finally:
    if f:
        f.close()


with open('//','r') as f:
    print(f.read())

"""
read()
read(size)
readline()
readlines()
"""

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉


f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')

