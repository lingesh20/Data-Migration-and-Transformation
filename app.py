import downloadfile as file
import extractfile as extract
import exportfiletoS3 as exporttoS3
import s3toRds as s3rds

def main():
    
    file.file_download()

    extract.extract_file()

    local_file_path = 'C:\Users\linge\OneDrive\Documents\capstone2\CIK0000000013.json'
    bucket_name = 'capproject2'
    filename = local_file_path.split('/')[-1]
    s3_key = filename

    exporttoS3.upload_file_to_s3(local_file_path,bucket_name,s3_key)

    result = s3rds.s3_to_RDS(bucket_name,filename)

    print(result)

if __name__ == "__main__":
    main()