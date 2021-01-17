import fastjsonschema

import event_schemas


# defines fastjsonschema validators to use for validaton of the events
def get_validators():
    validators_by_schema_name = dict()
    for schema_name, schema in vars(event_schemas).items():
        if not schema_name.startswith("__"):
            if not isinstance(schema, dict):
                raise Exception(f"variable {schema_name} in event_schemas.py file must be a dict")

            validators_by_schema_name[schema_name] = fastjsonschema.compile(schema)

    return validators_by_schema_name
