from flask import Flask

def lambda_handler(event, context):
    first_name = event['queryStringParameters']['first_name']
    last_name = event['queryStringParameters']['last_name']
    message = 'Hello {} {}!'.format(first_name, last_name)
    return { 
        'message' : message
    }


