import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.update_table(
    TableName='student_performance',

    AttributeDefinitions=[
        {
            'AttributeName': 'grade',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'total_score',
            'AttributeType': 'N'
        }
    ],

    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'GradeScoreIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'grade',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'total_score',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                
            }
        }
    ]
)

print("GSI creation started")
response = dynamodb.describe_table(TableName='student_performance')

indexes = response['Table'].get('GlobalSecondaryIndexes', [])

for index in indexes:
    print(index['IndexName'], "=>", index['IndexStatus'])