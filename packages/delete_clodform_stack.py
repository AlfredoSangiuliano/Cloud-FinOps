import boto3
import sys

def delete_cloudformation_stack(stack_name):
    # Crear un cliente para CloudFormation
    client = boto3.client('cloudformation')

    try:
        # Eliminar el stack
        response = client.delete_stack(StackName=stack_name)

        # Esperar hasta que el stack sea eliminado
        waiter = client.get_waiter('stack_delete_complete')
        print(f"Eliminando el stack: {stack_name}...")
        waiter.wait(StackName=stack_name)

        print(f"Stack '{stack_name}' eliminado con éxito.")
    except client.exceptions.ClientError as e:
        print(f"Error al eliminar el stack: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python delete_stack.py <nombre_del_stack>")
        sys.exit(1)

    stack_name = sys.argv[1]
    delete_cloudformation_stack(stack_name)
