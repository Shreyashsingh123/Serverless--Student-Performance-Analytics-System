import boto3

s3 = boto3.client('s3')

file_path ="../../data/data.csv"   # your local CSV file

bucket_name = "student-performance-25"
s3_key = "raw/sample.csv"

s3.upload_file(
    file_path,
    bucket_name,
    s3_key
)

print("File uploaded successfully!")