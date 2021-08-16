import json


def lambda_handler(event, context):
    print("test1")
    print("test2")
    return {
        'statusCode': 200,
        'body': json.dumps("Demo")
    }
