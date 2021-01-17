"""
An example mqtt publisher to test the pipeline.
Just run the file as 'python publish.py'
"""

import json

import paho.mqtt.client as mqtt  # import the client1
from bson import ObjectId

topic = "events/temp_sensor"

broker_host = 'localhost'
client = mqtt.Client(str(ObjectId))  # create new instance
client.connect(broker_host, 1883)  # connect to broker

data = {
    "temperature": 1,
    "timestamp": "2018-11-13T20:20:39+00:00"
}
client.publish("events/temp_sensor", json.dumps(data), qos=0)