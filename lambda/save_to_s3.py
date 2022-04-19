import boto3
import os


# Create an S3 event
s3 = boto3.client("s3")
bucket_name = event['Records'][0]['s3']['bucket']['name']


def save_to_s3_handler(event, context):
	pass
