import boto3

s3 = boto3.client('s3')

file_path ="../../data/data.csv"   

bucket_name = "student-performance-25"
s3_key = "raw/student_performance_200.csv"

s3.upload_file(
    file_path,
    bucket_name,
    s3_key
)

print("File uploaded successfully!")