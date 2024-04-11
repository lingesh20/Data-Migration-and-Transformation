import downloadfile as file
import extractfile as extract
import exportfiletoS3 as exporttoS3
import s3toRds as s3rds
import os

def main():
    
    file.file_download()

    extract.extract_file()

    local_file_path = 'C:/Users/linge/OneDrive/Documents/capstone2/inputfiles'
    bucket_name = 'guviproject2'

    for filename in os.listdir(local_file_path):
        if filename.endswith(".json"):
            # Construct local file path
            file_path  = os.path.join(local_file_path, filename)
            
            # Use the filename as the S3 key
            s3_key = filename
            
            # Upload the file to S3
            exporttoS3.upload_file_to_s3(file_path, bucket_name, s3_key)

            result = s3rds.s3_to_RDS(bucket_name,filename)

            print(result)

if __name__ == "__main__":
    main()