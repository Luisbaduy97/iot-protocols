from paho.mqtt import client as mqttClient
import time

def on_connect(client, userdate, flags, rc):
    if rc == 0:
        print('Connected')
        global Connected
        Connected = True
    else:
        print('Not connected')
    return

def on_message(client, userdata, message):
    print(message.topic, message.payload)
    return

Connected = False
broker_address = 'broker.hivemq.com'
port = 1883

tag = "/MNA/IOT/LN34/#"

client1 = mqttClient.Client('cliente')
client1.on_connect = on_connect
client1.on_message = on_message
client1.connect(broker_address, port)
client1.loop_start()

while Connected != True:
    time.sleep(0.1)
    client1.subscribe(tag)
    try:
        while True:
            time.sleep(1)
    except:
        client1.disconnect()
        client1.loop_stop()