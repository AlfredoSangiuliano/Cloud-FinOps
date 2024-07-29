import boto3
from pprint import pprint
# Dictionary with AWS products, platforms and services.

pps = {}

def list_s3_buckets():
    # Create s3 client instance
    s3_client = boto3.client('s3')

    try:
        # Llamar a list_buckets para obtener todos los buckets
        response = s3_client.list_buckets()

        # Mostrar los nombres de los buckets
        # print("Buckets en tu cuenta de S3:")
        for bucket in response['Buckets']:
            pps['s3'] = [{bucket['Name']}]

    except boto3.exceptions.Boto3Error as e:
        print(f"Error al listar los buckets: {e}")

pprint(list_s3_buckets())