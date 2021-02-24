import paho.mqtt.client as mqtt
import time
import random
import json

broker = "localhost"
port = 1883
topic =  "LENZDRGB611"
msg_string = '{"temp": 20, "location": "LENZDRGB611", "type": "temperature", "units":  {"temp": "° C"}}'
msg_json = json.loads(msg_string)

#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('testtopic/#')

# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# send random temperature values to mqtt topic
def publish(client):    
     while True:
         time.sleep(random.randint(1, 10))
         msg_json["temp"] = round(random.uniform(20, 30), 2)
         msg_payload = json.dumps(msg_json)
         result = client.publish(topic, payload="test",qos=0, retain=False)
         # result: [0, 1]
         status = result[0]
         if status == 0:
             print(f"Send `{msg_json}` to topic `{topic}`")
         else:
             print(f"Failed to send message to topic {topic}")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)


         
publish(client)
client.loop_forever()