import boto3
import sys

def delete_s3_bucket(bucket_name):
    # Crear un cliente para S3
    s3_client = boto3.client('s3')

    try:
        # Listar y eliminar todos los objetos del bucket
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    print(f"Eliminando objeto {obj['Key']}...")
                    s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])

        # Listar y eliminar todas las versiones de objetos (si el bucket tiene versioning habilitado)
        paginator = s3_client.get_paginator('list_object_versions')
        for page in paginator.paginate(Bucket=bucket_name):
            if 'Versions' in page:
                for version in page['Versions']:
                    print(f"Eliminando versión {version['Key']}...")
                    s3_client.delete_object(Bucket=bucket_name, Key=version['Key'], VersionId=version['VersionId'])
            if 'DeleteMarkers' in page:
                for delete_marker in page['DeleteMarkers']:
                    print(f"Eliminando delete marker {delete_marker['Key']}...")
                    s3_client.delete_object(Bucket=bucket_name, Key=delete_marker['Key'], VersionId=delete_marker['VersionId'])

        # Eliminar el bucket
        print(f"Eliminando el bucket {bucket_name}...")
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' eliminado con éxito.")
    except boto3.exceptions.S3UploadFailedError as e:
        print(f"Error al eliminar el bucket: {e}")
    except boto3.exceptions.Boto3Error as e:
        print(f"Error al eliminar el bucket: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python delete_bucket.py <nombre_del_bucket>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    delete_s3_bucket(bucket_name)
