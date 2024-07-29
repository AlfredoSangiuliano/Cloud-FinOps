import boto3

def list_sagemaker_domains():
    # Create a SageMaker client
    sagemaker_client = boto3.client('sagemaker')

    try:
        # Call list_domains to get all domains
        response = sagemaker_client.list_domains()

        # Print information about each domain
        print("SageMaker Domains:")
        for domain in response['Domains']:
            print(f"Domain ID: {domain['DomainId']}")
            print(f"Domain ARN: {domain['DomainArn']}")
            print(f"Domain Name: {domain['DomainName']}")
            print(f"Status: {domain['Status']}")
            print(f"Creation Time: {domain['CreationTime']}")
            print(f"Last Modified Time: {domain['LastModifiedTime']}")
            print("\n")
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing SageMaker domains: {e}")

if __name__ == "__main__":
    list_sagemaker_domains()