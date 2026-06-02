import boto3

s3 = boto3.client('s3')

file_path ="../../data/student_data.json"   
# file_path ="../../data/student_data.csv" 
bucket_name = "student-performance-25"
s3_key = "raw/student_data.json"
# s3_key = "raw/student_data.csv"
s3.upload_file(
    file_path,
    bucket_name,
    s3_key
)

print("File uploaded successfully!")