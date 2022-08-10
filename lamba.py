import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    db_count = {}
    db_count = client.get_item(
        TableName='Cloud_Resume',
        Key={
            'id': {
                'S': 'count'
            }
        })
    old_count = db_count['Item']['value']['S']
    new_count = int(old_count) + 1
    new_count = str(new_count)
    print(new_count)
    
    client.put_item(
        TableName='Cloud_Resume',
        Item={
            'id': {
                'S': 'count'
            },
            'value': {
                'S': new_count
            }
            })
    
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['headers']['Access-Control-Allow-Headers'] = 'Content-Type'
    responseObject['headers']['Access-Control-Allow-Origin'] = '*'
    responseObject['headers']['Access-Control-Allow-Methods'] = 'GET,OPTIONS'
    responseObject['body'] = new_count
    return responseObject
