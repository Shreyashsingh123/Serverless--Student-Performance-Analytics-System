import csv
import boto3
from decimal import Decimal

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('student-performance')

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

        total_score = Decimal(row['total_score'])

        if total_score > Decimal('90'):
            performance_category = "Excellent"
        elif total_score >= Decimal('75'):
            performance_category = "Good"
        elif total_score >= Decimal('60'):
            performance_category = "Average"
        else:
            performance_category = "Poor"

        table.put_item(
            Item={
                'student_id': int(row['student_id']),
                'weekly_self_study_hours': int(row['weekly_self_study_hours']),
                'attendance_percentage': int(row['attendance_percentage']),
                'class_participation': int(row['class_participation']),
                'total_score': total_score,
                'grade': row['grade'],
                'performance_category': performance_category
            }
        )

    return {
        'statusCode': 200
    }