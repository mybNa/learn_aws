import json


def hello_world_hanlder(event, context):
	return {
		"statusCode": 200,
		"body": "THIS IS standard hello world"
	}
