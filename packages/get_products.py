import boto3
from pprint import pprint
# Dictionary with AWS products, platforms and services.

pps = {}

def list_s3_buckets():
    counter = 0
    s3_client = boto3.client('s3')

    try:
        # Call list_cuckets to get buckets: 
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            counter += 1
            pps[f'Bucket {str(counter)}'] = bucket['Name']
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing buckets: {e}")
    return pps


def list_lambda_functions():
    # Create a Lambda client
    counter = 0
    lambda_client = boto3.client('lambda')

    try:
        # Call list_functions to get all Lambda functions
        response = lambda_client.list_functions()

        # Print information about each function
        for function in response['Functions']:
            counter += 1
            pps[f'Lambda Function {str(counter)}'] = function['FunctionName']
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing Lambda functions: {e}")


pprint(list_s3_buckets())
