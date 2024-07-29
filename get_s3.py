import boto3

def list_s3_buckets():
    # Crear un cliente para S3
    s3_client = boto3.client('s3')

    try:
        # Llamar a list_buckets para obtener todos los buckets
        response = s3_client.list_buckets()

        # Mostrar los nombres de los buckets
        print("Buckets en tu cuenta de S3:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
    except boto3.exceptions.Boto3Error as e:
        print(f"Error al listar los buckets: {e}")

if __name__ == "__main__":
    list_s3_buckets()
