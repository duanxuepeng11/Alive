
from kafka import KafkaProducer
from time import sleep
import json
import random
import datetime

'''
    生产者demo
    向test_lyl2主题中循环写入10条json数据
    注意事项：要写入json数据需加上value_serializer参数，如下代码
'''
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers=['192.168.121.41:6667','192.168.121.42:6667','192.168.121.43:6667']
)
arr = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","11","22"
    ,"23","24"]
for i in range(100):
    ##生成user_id
    userId = random.randint(10000,100000)
    dd = datetime.datetime.now()
    data={
        "country":"中国",
        "event_code":"payment"+str(random.randint(0,2)),
        "channel":"moren",
        "user_id":userId,
        # "stat_time":"2019-07-02 "+arr[random.randint(0,23)]+":00:00",
        "stat_time":"2019-07-02 04:00:00",
        "key_1":1,
        "key_2":2,
        "key_3":3,
        "app_version":i,
        "appkey":"dxdsadsdsadsa2342asdas"+str(random.randint(0,2))
    }
    print(data)
    #import_logs
    producer.send('axt1', data)
    # sleep(1)
    print("xxx%d" % i)
    producer.flush()
