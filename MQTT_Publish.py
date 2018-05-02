# MQTT Publish

import paho.mqtt.publish as publish

# Publish test string touch to topic topic/display1
publish.single("topic/display1", "touch", hostname="test.mosquitto.org")

# Publish test string swipe to topic topic/display2
publish.single("topic/display2", "swipe", hostname="test.mosquitto.org")
