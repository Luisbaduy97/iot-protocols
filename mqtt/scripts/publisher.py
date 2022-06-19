import pandas as pd
from paho.mqtt import client as mqttClient
import time

dataframe = pd.read_csv('DatosPruebaMQTT.csv', index_col=0)
dataframe.head()

dataframe.describe(include='all')

df = dataframe.dropna()

temp = df['Temperature'].tolist()
hum = df['Humidity'].tolist()
co = df['CO2'].tolist()

def on_connect(client, userdate, flags, rc):
    if rc == 0:
        print('Connected')
        global Connected
        Connected = True
    else:
        print('Not connected')
    return


Connected = False
broker_address = 'broker.hivemq.com'
port = 1883
tag1 = "/MNA/IOT/LN34/Temp" #TOPIC
tag2 = "/MNA/IOT/LN34/Humid" #TOPIC
tag3 = "/MNA/IOT/LN34/CO2" #TOPIC
client = mqttClient.Client('Python')
client.on_connect = on_connect

while Connected != True:
    time.sleep(0.1)
    try:
        for i, j, k in zip(temp, hum, co):
            v1, v2, v3 = '{"Temperatura": "'+str(i)+'" }', '{"Humedad": "'+str(j)+'" }', '{"CO2": "'+str(k)+'" }'
            print(v1, '\n',v2, '\n', v3)
            client.publish(tag1, v1, qos=2)
            client.publish(tag2, v2, qos=2)
            client.publish(tag3, v3, qos=2)
            time.sleep(2)
    except KeyboardInterrupt:
        print('Envio datos')
        client.disconnect()
        client.loop_stop()