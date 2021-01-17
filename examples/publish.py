"""
An example mqtt publisher to test the pipeline.
Just run the file as 'python publish.py'
"""

import json

import paho.mqtt.client as mqtt  # import the client1
from time import time, sleep
from bson import ObjectId

broker_host = 'localhost'
client = mqtt.Client(str(ObjectId))  # create new instance
client.connect(broker_host, 1883)  # connect to broker


def publish_data():
    for i in range(10):
        data = {
            "temperature": 1,
            "timestamp": "2018-11-13T20:20:39+00:00"
        }
        client.publish("events/tempsensor".format(str(i)), json.dumps(data), qos=0)
        # print(i)
        sleep(0.0001)


start = time()
publish_data()
print("took: ", time() - start)
