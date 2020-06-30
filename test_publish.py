#!/usr/bin/env python3
import argparse
import paho.mqtt.client as mqttc
import random
# Read the host address and port number of the broker

parser = argparse.ArgumentParser()
parser.add_argument("--broker", "-b", default="localhost", help="IP address of the broker", type=str)
parser.add_argument("--port", "-p", default=1883, help="Port number of the broker", type=int)
parser.add_argument("--topic", "-t", default="test", help="Topic to subscribe to", type=str)
parser.add_argument("--qos", default=0, help="QoS for the publish function", type=int)
parser.add_argument("--serial", "-s", default="/dev/ttyACM0", help="Serial path to Arduino", type=str)
parser.add_argument("--message", "-m", default="First message Published", help="message to subscriber", type=str)

args = parser.parse_args()


# Callback for the CONNACK from the server
def connect_callback(client, userdata, flags, reasonCode, properties):
    print("Connected to server with code "+str(reasonCode))
    pass


# Define the callback for publication (something to do once it's done)
def publish_callback(client,userdata,mid):
    print("All done publishing mid: ", mid)
    pass

def message_callback(client, userdata, msg):
    print(msg.topic,msg.payload, "QoS: ", msg.qos)
    pass

if __name__== "__main__" :
    client = mqttc.Client("Prashant : Random_message_test")
    client.on_connect = connect_callback
    client.on_publish = publish_callback
    client.on_message = message_callback
    # Auth
    # Last will and testament
    client.username_pw_set("publisher", "password")

    client.will_set(args.topic, "emergency""This is Last will message : unexpected disconnection from client", qos=0,retain=False)
    # client.reconnect_delay_set(5)

    client.connect(args.broker, args.port)
    payld = str(args.message)
    # q_s = str(args.qos)
    # client.loop_start()
    ret = client.publish(args.topic, payload=payld, qos=args.qos)
    if not ret.is_published(): 
        # client.reconnect(args.broker, args.port)
        ret.wait_for_publish()
        # client.loop_stop()
    # client.disconnect(reasoncode=0)
    else:
        client.disconnect(reasoncode=1)    