import os
print(os.name)
# os.uname()
# print(os.environ)
print(os.environ.get('JAVA_HOME'))

print(os.path.abspath("."))
#再第一个参数下创建文件夹
os.path.join(os.path.abspath("."), 'testdir')
os.mkdir(os.path.abspath(".")+"/testdir")
# os.rmdir('/Users/michael/testdir')







