import csv
import boto3
from decimal import Decimal

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('student_performance')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    lines = obj['Body'].read().decode('utf-8').splitlines()
    reader = csv.DictReader(lines)

    for row in reader:

        print("Processing:", row['student_id'])

        total_score = Decimal(str(row['total_score']))
        if total_score > Decimal('90'):
            performance_category = "Excellent"
        elif total_score >= Decimal('75'):
            performance_category = "Good"
        elif total_score >= Decimal('60'):
            performance_category = "Average"
        else:
            performance_category = "Poor"

        # your logic

        table.put_item(
            Item={
                'student_id': str(row['student_id']),
                'weekly_self_study_hours': Decimal(str(row['weekly_self_study_hours'])),
                'attendance_percentage': Decimal(str(row['attendance_percentage'])),
                'class_participation': Decimal(str(row['class_participation'])),
                'total_score': total_score,
                'grade': row['grade'],
                'performance_category': performance_category
            }
        )

        print("Inserted:", row['student_id'])

    return {
        'statusCode': 200,
        'body': 'CSV processed successfully'
    }