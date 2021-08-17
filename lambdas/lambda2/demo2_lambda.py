import json


def lambda_handler(event, context):
    print("demo_2 test1")
    print("demo_2 test2")
    print("demo_2 test3")
    return {
        'statusCode': 200,
        'body': json.dumps("Demo lambda 2")
    }
