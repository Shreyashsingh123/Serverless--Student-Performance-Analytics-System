import boto3
from dotenv import load_dotenv
import os
load_dotenv()
s3=boto3.client('s3')
region='ap-south-1'
bucket_name=os.getenv('bucket_name')
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
    'LocationConstraint':region
    }
)
print("bucket created successfully")