# mqtt-collector
 
mqtt-collector is an MQTT-based data pipeline that ingests data from MQTT publishers. It uses user-defined json-schemas for data validation and MongoDB for storing the validated data.
### How does it work?
- The json schema of the event to send to the pipeline is defined in **event_schemas.py**
- Event is published to an MQTT broker.
- The MQTT client in the pipeline subscribes to the defined events.
- The published events are inserted to MongoDB if compatible with the defined json schema. 

### Core dependencies
  - **Python version:** 3.7
  - **Storage:** MongoDB
  - **MQTT broker:** Any MQTT broker is fine, but i recommend EMQX. You can install it by following the instructions here: https://docs.emqx.io/en/broker/latest/getting-started/install.html <br />
  or you can install it in a docker container by running:
```sh
$ sudo docker run -d --name emqx -p 18083:18083 -p 1883:1883 emqx/emqx:latest
```

##  How to install and run?
  #### 1. Configurations
The project reads the configurations from a **.env** file. Create a file with the name **.env** in the project's folder and insert the following necessary configuration values as: 
 ```
MQTT_BROKER_HOST=localhost
MQTT_BROKER_PORT=1883
MONGO_CONN_STR=mongodb://localhost/events
```
#### 2. Install the packages
Create a virtual environment outside project and install the necessary packages. 
 ```sh
$ virtualenv -p python3.7 venv
$ source venv/bin/activate
$ cd mqtt-collector/
$ pip install -r requirements.txt
```
#### 3. Run
- In the project's folder, you can simply run the project as:
 ```sh
$ python run.py
```
If you see **MQTT Connection Successful** in console logs, that means you are successfully connected to the broker.

##  How to define an event schema and send data to the pipeline?
- To define your json schemas to validate your events, put your schemas one under the other as dictionaries in json-schema format in **event_schemas.py** file  which is in the project's top folder.
<br />
 ```
python
# example event_schemas.py file
temp_sensor = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "temperature": {
            "type": "number"
        },
        "timestamp": {
            "type": "string",
            "format": "date-time"
        }
    },
    "additionalProperties": False,
    "required": ["temperature", "timestamp"]
}
pressure_sensor = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "pressure": {
            "type": "number"
        },
        "timestamp": {
            "type": "string",
            "format": "date-time"
        }
    },
    "additionalProperties": False,
    "required": ["temperature", "timestamp"]
}
```
- To send your event to the pipeline, you must use an mqtt publisher. The mqtt topic must be in **events/<schema_name>** format. For example, if you defined your schema as **temp_sensor** in your **event_schemas.py** file, then **events/temp_sensor** must be the topic to publish to. Note that the event's payload must be **json formatted string**.
<br />
Here is an example publisher:
```python
"""An example event publisher"""
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
```
##  Where are the events stored?
- If the events are compatible with their pre-defined schemas, they are stored on your MongoDB under **events** database. The name of the collections they are inserted into are the same as the name of the schema. For example, if an event's schema name is **temp_sensor**, it is inserted under the collection with the name **temp_sensor**.

## TODO
- Rest api to define schemas.
- Authentication.
...
