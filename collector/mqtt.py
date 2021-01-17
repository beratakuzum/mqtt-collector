"""
MQTT Client Callbacks
"""

from collector.queues import DataQueue

import logging

logging.basicConfig(level=logging.INFO)


# The callback that works when the client successfully connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    logging.info("MQTT Connection Successful")
    client.subscribe('events/#')


# The callback that works when the client gets a new message from the broker
def on_message(client, userdata, msg):
    schema_name = msg.topic.split('/')[1]
    DataQueue.get_instance().add(event=msg.payload, schema_name=schema_name)
