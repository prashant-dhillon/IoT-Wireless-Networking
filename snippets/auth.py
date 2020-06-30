import paho.mqtt.client as mqttc
import random

client = mqttc.Client("Lamp")

# Auth: make sure that our broker has included these credentials
# Follow the steps using mosquitto_passwd and declaring the file 
# to our broker using the configuration file option for passwords
client.username_pw_set("user", "mySuperPassword")

client.connect("mqtt.eclipse.org", 1883, 60)
payld = str(random.randint(1,100))
client.loop_start()
ret = client.publish(args.topic, payload=payld, qos=args.qos)
if not ret.is_published(): 
    ret.wait_for_publish()
    client.loop_stop()
    print("Mission accomplished")
    client.disconnect(reasoncode=0)
else:
    print("Something went wrong")
    client.disconnect(reasoncode=1)    