



import time
import paho.mqtt.client as paho
from paho import mqtt

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# Callback to see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))
    print("Hello from MQTT")  # Print hello message after publishing

# Create an MQTT client instance
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)

# Assign the callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# Set username and password for the MQTT connection
client.username_pw_set("MANIK", "DDbb11$$")

# Connect to HiveMQ Cloud on port 8883 (default for secure MQTT)
client.connect("d26b08db913c4175923fbbec8b4fba32.s1.eu.hivemq.cloud", 8883)

# Publish a message to a specific topic
client.publish("encyclopedia/temperature", payload="hot", qos=1)

# Start the loop to process network traffic
client.loop_start()

# Give some time to publish the message and see the output
time.sleep(2)

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()
