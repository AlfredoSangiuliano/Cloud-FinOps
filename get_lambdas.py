import boto3

def list_lambda_functions():
    # Create a Lambda client
    lambda_client = boto3.client('lambda')

    try:
        # Call list_functions to get all Lambda functions
        response = lambda_client.list_functions()

        # Print information about each function
        print("AWS Lambda Functions:")
        for function in response['Functions']:
            print(f"Function Name: {function['FunctionName']}")
            print(f"Function ARN: {function['FunctionArn']}")
            print(f"Runtime: {function['Runtime']}")
            print(f"Handler: {function['Handler']}")
            print(f"Last Modified: {function['LastModified']}")
            print("\n")
    except boto3.exceptions.Boto3Error as e:
        print(f"Error listing Lambda functions: {e}")

if __name__ == "__main__":
    list_lambda_functions()