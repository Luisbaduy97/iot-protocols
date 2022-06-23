#!/usr/bin/env python
import pika
import sys
import pandas as pd
import json
import time

df = pd.read_csv('../data/sensor_data.csv')

cols = df.columns.values.tolist()
rows = df.values.tolist()
# amqps://ryqzcgot:XU4yfegqzEjoBu5_wKdwgYrGic68TRSR@gull.rmq.cloudamqp.com/ryqzcgot # E
# amqps://tppeqnwn:OchMIE3eLF0K3Yl4NBlwDHhRhgGwWLvk@shrimp.rmq.cloudamqp.com/tppeqnwn # L
params = pika.URLParameters('amqps://tppeqnwn:OchMIE3eLF0K3Yl4NBlwDHhRhgGwWLvk@shrimp.rmq.cloudamqp.com/tppeqnwn')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

#message = ' '.join(sys.argv[1:]) or "Hello World!"

for i in range(len(rows)):
    body = json.dumps({v: str(j) for (v, j) in zip(cols, rows[i])})
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=body,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE # read docs
        ))
    time.sleep(2)
    print(" [x] Sent %r" % body)
connection.close()
