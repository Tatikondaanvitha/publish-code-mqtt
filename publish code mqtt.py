# Import package
import paho.mqtt.client as mqtt
# Define Variables
MQTT_BROKER = "192.168.43.187" # IP address of pi
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45 #seconds to keep alive
MQTT_TOPIC = "bhavskanvi"
MQTT_MSG = "we are from thunders batch........."

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
    print ("Connected to MQTT Broker")
    
# Define on_publish event Handler
def on_publish(client, userdata, mid):
    print ("Message Published...")
    
# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Publish message to MQTT Topic
mqttc.publish(MQTT_TOPIC,MQTT_MSG)
# Disconnect from MQT
