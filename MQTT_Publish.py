# MQTT Publish

import paho.mqtt.publish as publish

# Publish test string Touch to topic topic/touch
publish.single("topic/touch", "Touch", hostname="test.mosquitto.org")

# Publish test string Swipe to topic topic/swipe
publish.single("topic/swipe", "Swipe", hostname="test.mosquitto.org")
