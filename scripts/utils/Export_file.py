import boto3
import csv
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student_performance')

def export_data(file_name):

    response = table.scan()
    items = response['Items']

    extension = file_name.split('.')[-1].lower()
    if extension == 'csv':

        with open(file_name, 'w', newline='') as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    'student_id',
                    'weekly_self_study_hours',
                    'attendance_percentage',
                    'class_participation',
                    'total_score',
                    'grade',
                    'performance_category'
                ]
            )

            writer.writeheader()
            writer.writerows(items)

        print("CSV file exported successfully")

    elif extension == 'json':

        class DecimalEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, Decimal):
                    return float(obj)
                return super().default(obj)

        with open(file_name, 'w') as file:
            json.dump(
                items,
                file,
                indent=4,
                cls=DecimalEncoder
            )

        print("JSON file exported successfully")

    else:
        print("Unsupported file format")

export_data("../../data/student_data.csv")
export_data("../../data/student_data.json")