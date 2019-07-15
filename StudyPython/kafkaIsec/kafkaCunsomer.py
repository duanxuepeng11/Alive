from kafka import KafkaConsumer
import json

'''
    消费者demo
    消费test_lyl2主题中的数据
    注意事项：如需以json格式读取数据需加上value_deserializer参数
'''


consumer = KafkaConsumer('axt1',group_id="data_form_mysql-gid1",
                         bootstrap_servers=['192.168.121.41:6667','192.168.121.42:6667','192.168.121.43:6667'],
                         auto_offset_reset='earliest',value_deserializer=json.loads
                         )
for message in consumer:
    print(message.value)
