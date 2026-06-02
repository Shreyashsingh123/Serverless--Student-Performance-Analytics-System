import boto3

dynamodb=boto3.resource('dynamodb')
dynamodb.create_table(
    TableName='student_performance',
    KeySchema=[
        {
            'AttributeName':'student_id',
            'KeyType':'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName':'student_id',
            'AttributeType':'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)
print("table created successfully")