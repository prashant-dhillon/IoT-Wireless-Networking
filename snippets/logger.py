
import logging
import paho.mqtt.client as mqtt

logging.basicConfig(level=logging.DEBUG)

mqttc = mqtt.Client()

logger = logging.getLogger(__name__)
mqttc.enable_logger(logger)

mqttc.connect("mqtt.eclipse.org", 1883, 60)

mqttc.subscribe("$SYS/#", 0)

mqttc.loop_forever()
