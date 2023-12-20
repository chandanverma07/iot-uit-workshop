import boto3

def upload_file_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name or file_name)
        print(f" image uploaded {file_name}")
    except ClientError as e:
        logging.error(e)
        return False
    return True

image="albert_1.jpg"
bucket_name="uit-data-bucket"
# Usage
upload_file_to_s3(image, bucket_name)
