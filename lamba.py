import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    #Retrieve current visitors number from DynamoDB
    db_count = {}
    db_count = client.get_item(
        TableName='Cloud_Resume',
        Key={
            'id': {
                'S': 'count'
            }
        })

    #Pull value from dictionary, increment by 1, assign to variable.
    old_count = db_count['Item']['value']['S']
    new_count = int(old_count) + 1
    new_count = str(new_count)
    
    #Place updated value back in table, replacing prior value.
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

    db_new_count = {}
    db_new_count = client.get_item(
        TableName='Cloud_Resume',
        Key={
            'id': {
                'S': 'count'
            }
        })
    
    #This if statement tests if the database values are being retrieved properly and that they are being updated in DynamoDB.
    if ((int(old_count) != int(new_count)) and (db_count['Item']['value']['S'] != db_new_count['Item']['value']['S'])):
        responseObject = {}
        responseObject['statusCode'] = 200
        responseObject['headers'] = {}
        responseObject['headers']['Content-Type'] = 'application/json'
        responseObject['headers']['Access-Control-Allow-Origin'] = 'https://brandon-daley.com'
        responseObject['body'] = new_count
    else:
        responseObject = {}
        responseObject['statusCode'] = 500
        responseObject['headers'] = {}
        responseObject['headers']['Content-Type'] = 'application/json'
        responseObject['headers']['Access-Control-Allow-Origin'] = 'https://brandon-daley.com'
        responseObject['body'] = "Database is not updating, please investigate."
    return responseObject