import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'POST':
        return create_student(event)
    elif http_method == 'GET':
        return get_student(event)
    elif http_method == 'PATCH':
        return update_student(event)
    elif http_method == 'DELETE':
        return delete_student(event)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported HTTP method')
        }

def create_student(event):
    try:
        body = json.loads(event['body'])
        student_id = body['StudentID']
        student_name = body['StudentName']
        program = body['Program']
        
        table.put_item(
            Item={
                'StudentID': student_id,
                'StudentName': student_name,
                'Program': program
            }
        )
        
        return {
            'statusCode': 201,
            'body': json.dumps('Student created successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def get_student(event):
    try:
        student_id = event['queryStringParameters']['StudentID']
        
        response = table.get_item(
            Key={
                'StudentID': student_id
            }
        )
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('Student not found')
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def update_student(event):
    try:
        body = json.loads(event['body'])
        student_id = body['StudentID']
        update_expression = 'SET '
        expression_attribute_values = {}
        
        if 'StudentName' in body:
            update_expression += 'StudentName = :name, '
            expression_attribute_values[':name'] = body['StudentName']
        
        if 'Program' in body:
            update_expression += 'Program = :program, '
            expression_attribute_values[':program'] = body['Program']
        
        update_expression = update_expression.rstrip(', ')
        
        table.update_item(
            Key={
                'StudentID': student_id
            },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Student updated successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def delete_student(event):
    try:
        student_id = event['queryStringParameters']['StudentID']
        
        table.delete_item(
            Key={
                'StudentID': student_id
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Student deleted successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }