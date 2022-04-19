import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def get_from_bucket(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        if not key.endswith('csv'):
            raise
        else:
            response = s3.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8')
            #print the content
            print('Content: ', content)

            return {
            	'statusCode': 200,
            	'body': json.dumps({'res': [content]})
            }
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
