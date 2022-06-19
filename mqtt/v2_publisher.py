from paho.mqtt import client as mqtt_client
import random
import time
import pandas as pd

dataframe = pd.read_csv('../data/DatosPruebaMQTT.csv', index_col=0)
dataframe.head()

dataframe.describe(include='all')

df = dataframe.dropna()

temp = df['Temperature'].tolist()
hum = df['Humidity'].tolist()
co = df['CO2'].tolist()

broker = 'broker.hivemq.com'
port = 1883
topic = "/python/mqtt"
client_id = 'PY_CLIENT_LJ'
tag1 = "/MNA/IOT/LN34/Temp" #TOPIC
tag2 = "/MNA/IOT/LN34/Humid" #TOPIC
tag3 = "/MNA/IOT/LN34/CO2" #TOPIC
# username = 'emqx'
# password = 'public'
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        for i, j, k in zip(temp, hum, co):
            v1, v2, v3 = '{"Temperatura": "'+str(i)+'" }', '{"Humedad": "'+str(j)+'" }', '{"CO2": "'+str(k)+'" }'
            c1 = client.publish(tag1, v1, qos=2)
            if c1[0] == 0:
             print(f"Send `{v1}` to topic `{tag1}`")
            else:
             print(f"Failed to send message to topic {tag1}")
            c2 = client.publish(tag2, v2, qos=2)
            if c2[0] == 0:
             print(f"Send `{v2}` to topic `{tag2}`")
            else:
             print(f"Failed to send message to topic {tag2}")
            c3 = client.publish(tag3, v3, qos=2)
            if c3[0] == 0:
             print(f"Send `{v3}` to topic `{tag3}`")
            else:
             print(f"Failed to send message to topic {tag3}")
            time.sleep(2)
            print('PUBLISHED')
        msg_count += 1
    

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

run()
