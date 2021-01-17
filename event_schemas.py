tempsensor = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'temperature': {
            "type": "number"
        },
        'timestamp': {
            "type": "string",
            "format": "date-time"
        }
    },
    "additionalProperties": False,
    'required': ['temperature', 'timestamp']
}