# Serverless Student Performance Analytics System

## Overview

This project is a **Serverless Student Performance Analytics System** built using AWS services and Python. The system automatically processes student performance datasets uploaded to Amazon S3, calculates performance metrics, stores records in DynamoDB, and supports analytical queries.

## Architecture

S3 Bucket → Lambda Function → DynamoDB

* **Amazon S3**: Stores uploaded student datasets.
* **AWS Lambda**: Processes uploaded files automatically.
* **Amazon DynamoDB**: Stores student performance records.
* **Python (Boto3)**: Used for data processing and CRUD operations.

## Features

### Data Processing

* Upload student datasets to S3.
* Automatic Lambda trigger on file upload.
* Parse JSON/CSV files.
* Calculate `performance_category`.
* Store records in DynamoDB.

### Performance Categories

| Total Score | Category  |
| ----------- | --------- |
| >= 90       | Excellent |
| 75 - 89     | Good      |
| 60 - 74     | Average   |
| < 60        | Poor      |

### Student Risk Detection

Students are marked as **at_risk = True** if:

* Attendance Percentage < 60
* OR Total Score < 50

### CRUD Operations

* Create student records
* Read student data by student_id
* Update student information
* Delete student records

### Query Operations

* Students with attendance > 90%
* Students with study hours > 10
* Students in Excellent category
* Top students using GSI

### Global Secondary Index (GSI)

* Partition Key: `grade`
* Sort Key: `total_score`

Used for:

* Retrieving top students in Grade A
* Finding highest-scoring students

### Data Export

* Export DynamoDB records to:

  * JSON
  * CSV
* Upload exported files to S3

## DynamoDB Table Schema

### Table Name

`student_performance`

### Attributes

* student_id
* weekly_self_study_hours
* attendance_percentage
* class_participation
* total_score
* grade
* performance_category
* at_risk

### Primary Key

* Partition Key: `student_id`

## Technologies Used

* Python
* AWS Lambda
* Amazon S3
* Amazon DynamoDB
* Boto3
* AWS IAM

## Project Structure

```text
project/
│
├── lambda/
│   └── lambda_function.py
│
├── scripts/
│   ├── crud_operations/
│   │   └── crud_operation.py
│   │   └── Advance_Task.py
│   │   └── query_operation.py
│   │
│   ├── utils/
│       └── create_bucket.py
│       └── create_table.py
│       └── Export_file.py
│       └──Global_Secondary_Index.py
│       └──trigger_function.py
│       └──upload_to_s3.py
│       └──trigger_function.zip
│      
│
├── data/
│   ├── student_dataset.csv
│   └── student_data.json
│   ├── data.csv
│   └── student_performance_200.csv
│
│
│
└──.gitignore
└── main.py
└──Readme.md
```

## Dataset

Student Performance Dataset containing:

* student_id
* weekly_self_study_hours
* attendance_percentage
* class_participation
* total_score
* grade

## Advanced Features

* Batch processing for large datasets (500+ records)
* Duplicate record handling
* Invalid JSON validation
* Missing field validation
* Top 10 student leaderboard

## Screenshots

Include screenshots of:

* S3 Bucket
* Lambda Function
* DynamoDB Table
* GSI Configuration
* Data Processing Results


