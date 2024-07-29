import boto3

def list_sagemaker_images():
    # Create a SageMaker client
    sagemaker_client = boto3.client('sagemaker')

    try:
        # Call list_images to get all SageMaker images
        response = sagemaker_client.list_images()

        # Print information about each image
        print("SageMaker Images:")
        for image in response['Images']:
            print(f"Image Name: {image['ImageName']}")
            print(f"Image ARN: {image['ImageArn']}")
            print(f"Creation Time: {image['CreationTime']}")
            print(f"Last Modified Time: {image['LastModifiedTime']}")
            print(f"Image Status: {image['ImageStatus']}")
            print("\n")
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing SageMaker images: {e}")

if __name__ == "__main__":
    list_sagemaker_images()
