# #!/usr/bin/python
# from sys import stdout, stdin
# import threading
# import subprocess
# from time import sleep
#
#
# shell = 'sh /usr/hdp/current/kafka-broker/bin/kafka-console-consumer.sh --zookeeper isec-hdp02:2181,isec-hdp03:2181,isec-hdp01:2181 --topic '
#
# topic = 'axt1'
#
# def send(msg):
#     stdout.write(msg + '\n')
#     stdout.flush()
#
# def receive():
#     global topic
#     #死循环
#     while True:
#         t = stdin.readline().strip()
#         if t != None and t != '':
#             topic = t
#             send('start monitoring topic: ' + topic)
#             break
#
# t0 = threading.Thread(target=receive)
# t0.start()
#
# def send_stuff():
#     while topic == None:
#         send('wait...')
#         sleep(2)
#     cmd = shell + topic
#     print cmd
#     p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, shell=True)
#     # 死循环
#     for line in iter(p.stdout.readline, b''):
#         send(line)
#     p.stdout.close()
#     p.wait()
#
# t1 = threading.Thread(target=send_stuff)
# t1.start()
#
# t0.join()
# t1.join()