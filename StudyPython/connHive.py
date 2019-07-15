#import pyhive as hive
from pyhive import hive

conn = hive.Connection('isec-hdp03',10000,'hive','default')
cur = conn.cursor()
cur.execute("select * from t1")
for result in cur.fetchall():
    print(result)