import boto3
import json

def show_buckets():
    s3 = boto3.client('s3')  
    response = s3.list_buckets()

    for bucket in response["Buckets"]:
       content =bucket["Name"]
       with open("aws_report", "w") as file:
           file.write(content)
       with open("aws_report", "r") as file:
           print(file.readline())
    
           
            
show_buckets()