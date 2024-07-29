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

        # Adding information about each function to lambdaF dict
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

        # Adding information about each domain to sagemakerdomains dict
        for domain in response['Domains']:
            sagemakerdomains[domain['DomainName']] = domain['CreationTime']
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing SageMaker domains: {e}")
    return sagemakerdomains

def list_sagemaker_images():
    # Create a SageMaker client
    sagemaker_client = boto3.client('sagemaker')

    try:
        # Call list_images to get all SageMaker images
        response = sagemaker_client.list_images()
        sagemakerimages = {}

        # Adding information about each imageto 
        print("SageMaker Images:")
        for image in response['Images']:
            sagemakerimages[image['ImageName']] = image['CreationTime']
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing SageMaker images: {e}")
    return sagemakerimages

def list_ec2_snapshots():
    # Crear un cliente para EC2
    ec2_client = boto3.client('ec2')
    ec2_snapshots = {}
    
    try:
        # Call describe_snapshots to get all snapshots
        response = ec2_client.describe_snapshots(OwnerIds=['self'])
        
        # Mostrar información sobre cada snapshot
        for snapshot in response['Snapshots']:
            ec2_snapshots[snapshot['SnapshotId']] = snapshot['StartTime']
    except boto3.exceptions.Boto3Error as e:
        print(f"Error al listar los snapshots: {e}")
    return ec2_snapshots

pps['Buckets'] = list_s3_buckets()
pps['Lambda'] = list_lambda_functions()
pps['SageMakerDomains'] = list_sagemaker_domains()
pps['SageMakerImages'] = list_sagemaker_images()
pps['EC2_snapshots'] = list_ec2_snapshots()

pprint(pps)