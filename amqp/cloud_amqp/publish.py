# publish.py
import pika, os
import pandas as pd
import json
import time

df = pd.read_csv('../../data/sensor_data.csv')

cols = df.columns.values.tolist()
rows = df.values.tolist()


# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
# url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters('amqps://tppeqnwn:OchMIE3eLF0K3Yl4NBlwDHhRhgGwWLvk@shrimp.rmq.cloudamqp.com/tppeqnwn')
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
#channel.basic_publish(exchange='',
#                      routing_key='hello',
#                      body='Hello CloudAMQP!')

#print(" [x] Sent 'Hello World!'")

for i in range(len(rows)):
    body = json.dumps({v: str(j) for (v, j) in zip(cols, rows[i])})
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=body
    )
    time.sleep(2)
    print(" [x] Sent %r" % body)


connection.close()