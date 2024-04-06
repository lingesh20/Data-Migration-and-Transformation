import boto3

def upload_file_to_s3(local_file_path, bucket_name, s3_key):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the file
    respomse = s3.upload_file(local_file_path, bucket_name, s3_key)

    print(respomse)