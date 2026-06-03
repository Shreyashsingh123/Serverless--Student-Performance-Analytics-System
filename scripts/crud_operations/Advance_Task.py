import boto3
import json
from decimal import Decimal
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student_performance')

class AdvancedOperations:

# 1. Student Risk Detection
    def student_risk_detection(self):
        response = table.scan()
        for item in response['Items']:
            attendance = Decimal(str(item['attendance_percentage']))
            score = Decimal(str(item['total_score']))
            at_risk = False
            if attendance < Decimal('60') or score < Decimal('50'):
                at_risk = True

            table.update_item(
                Key={
                    'student_id': item['student_id']
                },
                UpdateExpression='SET at_risk = :r',
                ExpressionAttributeValues={
                    ':r': at_risk
                }
            )

        print("Risk Detection Completed")

    #  Top 10 Performers
    def top_performers(self):

        response = table.scan()

        students = response['Items']

        students = sorted(
            students,
            key=lambda x: Decimal(str(x['total_score'])),
            reverse=True
        )

        print("\nTop 10 Students\n")

        for student in students[:10]:
            print(student)

    #  Batch Data Processing
    def batch_insert(self, records):

        with table.batch_writer() as batch:

            for record in records:

                batch.put_item(
                    Item=record
                )

        print("Batch Insert Completed")

    #  Invalid JSON Handling
    def validate_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

            print("Valid JSON File")

            return data

        except json.JSONDecodeError:
            print("Invalid JSON File")
            return None

    #  Missing Fields Handling
    def check_missing_fields(self, record):

        required_fields = [
            'student_id',
            'weekly_self_study_hours',
            'attendance_percentage',
            'class_participation',
            'total_score',
            'grade'
        ]
        for field in required_fields:
            if field not in record:
                print(f"Missing Field: {field}")
                return False
        return True

    #  Duplicate Student Detection
    def check_duplicate_student(self, student_id):

        response = table.get_item(
            Key={
                'student_id': student_id
            }
        )
        if 'Item' in response:
            print(
                f"Duplicate Record Found "
                f"for Student ID {student_id}"
            )
            return True

        return False