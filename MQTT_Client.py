# MQTT Client

import paho.mqtt.client as mqtt

# Callback when client receives respond from server
def on_connection(client, userdata, flags, rc):
        print("Connected successful "+str(rc))
        client.subscribe("topic/display1")
        client.subscribe("topic/display2")

# Callback when PUBLISH message is received 
def on_message(client, userdata, msg):
        #print(msg.topic +" "+str(msg.payload))
        if msg.payload == "touch":
                print("RECEIVED message: TOUCH")
        
        elif msg.payload == "swipe":
                print("RECEIVED message: SWIPE")
                
        elif msg.payload != "touch" or msg.payload != "swipe":
                print("Wrong command received: " + str(msg.payload) + " is not defiend.")

# Creates MQTT client and attaches custom functions
# invoke client class
myclient = mqtt.Client() 
myclient.on_connect = on_connection
myclient.on_message = on_message
# connect to OpenSource broker Mosquitto
myclient.connect("test.mosquitto.org", 1883, 60)
myclient.loop_forever()

