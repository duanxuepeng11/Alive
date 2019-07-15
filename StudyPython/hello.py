import random
import datetime
print("aaaa")
def foo():
    stu ="function"
    print(stu)

def fool(num):
    print("num" ,num)

if __name__ == '__main__':
    print("main")
    foo()
    fool(44)
    print(random.randint(10000,100000))
    now_time = datetime.datetime.now()
    print(now_time)