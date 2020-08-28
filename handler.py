import json


def hello(event, context):
    print('Test log message!')
    body = {
        "message": "Chris Dao wants to say hello to the World!",
        "event": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
