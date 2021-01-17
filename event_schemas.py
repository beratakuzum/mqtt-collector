"""Json schemas to validate events"""

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