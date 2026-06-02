import boto3
from decimal import Decimal
dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('student_performance')

def insert_item():
        
    table.put_item(
        Item={
                    'student_id': input("enter student_id"),
                    'weekly_self_study_hours': Decimal(input("Enter weekly self study hour")),
                    'attendance_percentage': Decimal(input("Enter attendance percentage")),
                    'class_participation': Decimal(input("enter class participation")),
                    'total_score': Decimal(input("enter total_Score")),
                    'performance_category':input("Enter the performance category: "),
                    'grade': input("Enter grade ")
        }
    )
    print("data inserted successfully")

def read_item():
    id = input("Enter the id: ")
    response=table.get_item(
        Key={
            "student_id":id
        }
    )
    print(response['Item'])

def update_item():
        id = input("Enter the id: ")

        print("\n1. Weekly Study Hours")
        print("2. Attendance Percentage")
        print("3. Class Participation")
        print("4. Total Score")
        print("5. Grade")

        choice = int(input("Select field to update: "))

        if choice == 1:
            field='weekly_self_study_hours'
            value = Decimal(input("Enter new study hours: "))
        elif choice == 2:
            field='attendance_percentage'
            value = Decimal(input("Enter new attendance percentage: "))

        elif choice == 3:
            field='class_participation'
            value = Decimal(input("Enter new class participation: "))
            
        elif choice == 4:
            field='total_score'
            value = Decimal(input("Enter new total score: "))
           
        elif choice == 5:
            field='grade'
            value = input("Enter new grade: ")
           

        response = table.update_item(
            Key={
                 'student_id': id
        },
        UpdateExpression=f"SET {field} = :v",
        ExpressionAttributeValues={
            ':v': value
        },
        ReturnValues="UPDATED_NEW"
        )
        print("\nRecord Updated Successfully")
        


def delete_item():
    id = input("Enter the id: ")
    table.delete_item(
        Key={
            'student_id':id
        }
    )
    print('data deleted successfully')

# insert_data('5000')
# read_data('5000')
# update('5000')
# read_data('5000')
    
