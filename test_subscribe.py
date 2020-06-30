#!/usr/bin/env python3
import argparse
import paho.mqtt.client as mqttc
# Read the host address and port number of the broker

parser = argparse.ArgumentParser()
parser.add_argument("--broker", "-b", default="localhost", help="IP address of the broker", type=str)
parser.add_argument("--port", "-p", default=1883, help="Port number of the broker", type=int)
parser.add_argument("--user", "-u", default="", help="Login for your broker [Optional]", type=str)
parser.add_argument("--password", "-P", help="Password for your broker [Optional]", type=str)
parser.add_argument("--topic", "-t", default="test", help="Topic to subscribe to", type=str)
parser.add_argument("--serial", "-s", default="/dev/ttyACM0", help="Serial path to Arduino", type=str)
args = parser.parse_args()

# Callback for the CONNACK from the server
def connect_callback(client, userdata, flags, rc, properties=None):
    print("Connected to server with code "+str(rc))
    print(mqttc.connack_string(rc))
    pass

# The callback for when a PUBLISH message is received from the server.
def message_callback(client, userdata, msg):
    # print(msg.topic,msg.payload)
    print(msg.topic,msg.payload)

    pass
    

if __name__== "__main__" :
    client = mqttc.Client("Security_Controler")
    client.on_connect = connect_callback
    client.on_message = message_callback
 
    if (len(args.user)==0) ^ (args.password is None) :
        print('Set either user and password or none of them!')
        exit(1)
    else:
        client.username_pw_set(args.user, args.password)
    
    client.connect(args.broker, args.port, keepalive=120)
    client.subscribe(args.topic)
    # client.subscribe("emergency")
    try:
        client.loop_forever()
        
    except KeyboardInterrupt:
        client.disconnect(reasoncode=0)
        print("Quitting...")