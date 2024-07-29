import boto3

def list_active_cloudformation_stacks():
    # Crear un cliente para CloudFormation
    client = boto3.client('cloudformation')

    # Llamar a describe_stacks para obtener todos los stacks
    response = client.describe_stacks()

    # Filtrar y mostrar los stacks activos
    for stack in response['Stacks']:
        stack_status = stack['StackStatus']
        if stack_status in ['CREATE_IN_PROGRESS', 
                            'CREATE_COMPLETE',
                            'ROLLBACK_IN_PROGRESS',
                            'ROLLBACK_COMPLETE',
                            'DELETE_IN_PROGRESS',
                            'UPDATE_IN_PROGRESS', 
                            'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 
                            'UPDATE_COMPLETE', 
                            'UPDATE_ROLLBACK_IN_PROGRESS', 
                            'UPDATE_ROLLBACK_FAILED', 
                            'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 
                            'UPDATE_ROLLBACK_COMPLETE', 
                            'REVIEW_IN_PROGRESS', 
                            'IMPORT_IN_PROGRESS', 
                            'IMPORT_COMPLETE', 
                            'IMPORT_ROLLBACK_IN_PROGRESS', 
                            'IMPORT_ROLLBACK_FAILED', 
                            'IMPORT_ROLLBACK_COMPLETE']:
            print(f"Stack Name: {stack['StackName']}, Status: {stack['StackStatus']}, Creation Time: {stack['CreationTime']}")

if __name__ == "__main__":
    list_active_cloudformation_stacks()
