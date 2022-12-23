import json
import boto3

#POST DATA
def saveData(event, context):
    print(event)
    body=json.loads(event["body"])
    client_dynamo=boto3.resource('dynamodb')
    table=client_dynamo.Table('weather')
    try:
        response=table.put_item(Item=body)
        return{
            'statusCode': 200,
            'body': json.dumps('City&Temp Added Successfully!')
              }
    except:
       raise

#DeleteData
# def deleteData(event, context):
#     data = json.loads(event['body'])
#     client_dynamo=boto3.resource('dynamodb')
#     table=client_dynamo.Table('weather')

#     result = table.delete_item(
#         Key={
#             'city': data['city'],
#             'temp': data['temp'],
#             'report': data['report']
#         }
#     )

#     # create a response
#     response = {
#         "statusCode": 200,
#          "body": "Data Deleted Successfully"    
#     }

#     return response

#UpdateData
def updateData(event, context):
    print(event)
    data = json.loads(event['body'])
    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('weather')  
    try:
        resuilt = table.update_item(
                Key={'city': data['city']
                   
                },
                UpdateExpression="SET report= :r",
                ExpressionAttributeValues={':r': data['report']},
                ReturnValues="UPDATED_NEW"
            )

        response = {
            "statusCode": 200,
            "body": json.dumps(resuilt['Attributes'])
        }
        return response
    except:
       raise



def deleteData(event, context):
    print(event)
    data = json.loads(event['body'])
    client_dynamo=boto3.resource('dynamodb')
    table=client_dynamo.Table('weather')

    result = table.delete_item(
        Key={
            'city': data['city']
            # 'temp': data['temp'],
            # 'report': data['report']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
         "body": "Data Deleted Successfully"    
    }

    return response


#GetData
def getData(event , context):
    print(event,".................")
    dynamodb=boto3.resource('dynamodb')
    table = dynamodb.Table('weather')
    result = table.scan()

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }
    return response

