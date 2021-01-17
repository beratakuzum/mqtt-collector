"""
An example mqtt publisher to test the pipeline.
Just run the file as 'python publish.py'
"""
import json
import uuid

import paho.mqtt.client as mqtt

topic = "events/temp_sensor"

broker_host = 'localhost'
client = mqtt.Client(str(uuid.uuid4()))  # create new client with a unique id
client.connect(broker_host, 1883)  # connect the to broker

data = {
    "temperature": 1,
    "timestamp": "2018-11-13T20:20:39+00:00"
}

# serializing json to str
formatted_data = json.dumps(data)
client.publish(topic, formatted_data, qos=0)