import paho.mqtt.client as mqtt


# Successful Connection Callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('testtopic/#')

# Message delivery callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()

# Set callback handler
client.on_connect = on_connect
client.on_message = on_message

# Set up connection
client.connect('broker.emqx.io', 1883, 60)
# Publish message
client.publish('emqtt',payload='Hello World',qos=0)

client.loop_forever()