import pymysql
#打开数据库连接
db= pymysql.connect("localhost","root","123456","test",3306)

cursor = db.cursor()
#获取游标
cursor.execute("select * from aaa")
results = cursor.fetchall()

#遍历结果
for row in results:
    print(row)
if __name__ == '__main__':
    print("aaa")

