import logging
import os
import uuid

import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from pymongo import MongoClient

from collector.mqtt import on_connect, on_message
from utils.scheduler import schedule_jobs
from utils.validators import get_validators

load_dotenv()
logging.basicConfig(level=logging.INFO)

logging.info("initializing mongo client")
client = MongoClient(os.getenv('MONGO_CONN_STR'))
mongo_db = client.get_database()

logging.info("initializing event inserter job")
validators_by_schema_name = get_validators()
schedule_jobs(mongo_db=mongo_db, validators_by_schema_name=validators_by_schema_name)

logging.info("initializing mqtt client")
client = mqtt.Client(client_id=str(uuid.uuid4()))
client.on_connect = on_connect
client.on_message = on_message
client.connect(os.getenv('MQTT_BROKER_HOST'), int(os.getenv('MQTT_BROKER_PORT')))
client.loop_forever()