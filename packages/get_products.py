import boto3
from pprint import pprint

# This dictionary will be populated with AWS products, platforms and services (pps).
pps = {}

def list_s3_buckets():
    buckets = {}
    s3_client = boto3.client('s3')

    try:
        # Call to list_buckets function: 
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            buckets[bucket['Name']] = bucket['CreationDate']
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing buckets: {e}")
    return buckets


def list_lambda_functions():
    # Create a Lambda client
    lambdaF = {}
    lambda_client = boto3.client('lambda')

    try:
        # Call list_functions to get all Lambda functions
        response = lambda_client.list_functions()

        # Print information about each function
        for function in response['Functions']:
            lambdaF[function['FunctionName']] = function['LastModified']
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing Lambda functions: {e}")
    return lambdaF

def list_sagemaker_domains():
    # Create a SageMaker client
    sagemaker_client = boto3.client('sagemaker')
    sagemakerdomains = {}

    try:
        # Call list_domains to get all domains
        response = sagemaker_client.list_domains()

        # Print information about each domain
        print("SageMaker Domains:")
        for domain in response['Domains']:
            sagemakerdomains[domain['DomainName']] = domain['CreationTime']
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing SageMaker domains: {e}")
    return sagemakerdomains


pps['Buckets'] = list_s3_buckets()
pps['Lambda'] = list_lambda_functions()
pps['SageMakerDomains'] = list_sagemaker_domains()

pprint(pps)