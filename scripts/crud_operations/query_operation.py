from decimal import Decimal
import boto3
from boto3.dynamodb.conditions import Attr
dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('student_performance')
class Query_Operation:
        
    def high_attendance_record():
        response=table.scan(
            FilterExpression=Attr('attendance_percentage').gt(90)
        )
        return response['Items']
    
    def weekly_self_study():
        response=table.scan(
            FilterExpression=Attr('weekly_self_study_hours').gt(10)
        )
        return response['Items']
    
    def get_excellent_students():
        response = table.scan(
            FilterExpression=Attr('performance_category').eq('Excellent')
        )
        return response['Items']



