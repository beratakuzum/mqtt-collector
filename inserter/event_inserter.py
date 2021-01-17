"""
Function that retrieves data from DataQueue, validates it by the schema and inserts into MongoDB.
"""

import logging
import json

from collector.queues import DataQueue


def initialize_event_inserter(**kwargs):
    logging.info("CURRENT DATA QUEUE SIZE: " + str(DataQueue.get_instance().size()))
    batch_limit = 30000
    mongo_db = kwargs['mongo_db']
    validators_by_schema_name = kwargs['validators_by_schema_name']

    events_grouped_by_schema_name = {}
    for i in range(batch_limit):
        _data = DataQueue.get_instance().get()
        if _data:
            event_raw = _data['event']
            schema_name = _data['schema_name']
            validator = validators_by_schema_name.get(schema_name)
            if not validator:
                logging.error(f"json schema for {schema_name} not found!!!")
                continue
            try:
                event_parsed = json.loads(event_raw)
                validator(event_parsed)

                if not events_grouped_by_schema_name.get(schema_name):
                    events_grouped_by_schema_name[schema_name] = [event_parsed]

                else:
                    events_grouped_by_schema_name[schema_name].append(event_parsed)

            except Exception as e:
                logging.error(f"{schema_name} event is not valid: " + str(e))
                continue

    for schema_name, events in events_grouped_by_schema_name.items():
        logging.info("number of documents that will be inserted: " + str(len(events)))
        mongo_db[schema_name].insert_many(events)
