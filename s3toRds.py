import boto3
import json
import pymysql

# Initialize the S3 client
s3 = boto3.client('s3')
rds_host = "database-1.cjka0akmyk2t.ap-south-1.rds.amazonaws.com"
username = "admin"
password = "admin123"
db_name = "finalproject"

def read_json_from_s3(bucket_name, key):
    try:
        # Get the JSON file object from S3
        obj = s3.get_object(Bucket=bucket_name, Key=key)
        # Read the contents of the file
        json_data = obj['Body'].read()
        # Parse the JSON data
        parsed_json = json.loads(json_data)
        return parsed_json
    except Exception as e:
        print(f"Error reading JSON file from S3: {e}")
        return None
    
def s3_to_RDS(bucketName,filename):
    try:
    # Replace 'your_bucket_name' and 'your_json_file_key' with the appropriate values
        bucket_name = bucketName
        json_file_key = filename

        # Read the JSON file from S3
        json_data = read_json_from_s3(bucket_name, json_file_key)

        # Print the JSON data
        # print(json_data)

        name = json_data['name']
        stateOfIncorporation = json_data['stateOfIncorporation']
        street1 = json_data['addresses']['business']['street1']
        street2 = json_data['addresses']['business']['street2']
        city = json_data['addresses']['business']['city']
        stateOrCountry = json_data['addresses']['business']['stateOrCountry']
        zipCode = json_data['addresses']['business']['zipCode']
        accessionNumber = json_data['filings']['recent']['accessionNumber']
        filingDate = json_data['filings']['recent']['filingDate']
        reportDate = json_data['filings']['recent']['reportDate']
        acceptanceDateTime = json_data['filings']['recent']['acceptanceDateTime']
        form = json_data['filings']['recent']['form']
        fileNumber = json_data['filings']['recent']['fileNumber']
        filmNumber = json_data['filings']['recent']['filmNumber']

        accessionNumber_str = ','.join(accessionNumber)
        filingDate_str = ','.join(filingDate)
        reportDate_str = ','.join(reportDate)
        acceptanceDateTime_str = ','.join(acceptanceDateTime)
        form_str = ','.join(form)
        fileNumber_str = ','.join(fileNumber)
        filmNumber_str = ','.join(filmNumber)

        conn = pymysql.connect(host=rds_host, user=username, password=password, database=db_name)
        cursor = conn.cursor()

        create_table_query = """
                CREATE TABLE IF NOT EXISTS customer (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    stateOfIncorporation VARCHAR(255),
                    street1 VARCHAR(255),
                    street2 VARCHAR(255),
                    city VARCHAR(255),
                    stateOrCountry VARCHAR(255),
                    zipCode VARCHAR(20),
                    accessionNumber VARCHAR(1500),
                    filingDate VARCHAR(1500),
                    reportDate VARCHAR(1500),
                    acceptanceDateTime VARCHAR(1500),
                    form VARCHAR(1500),
                    fileNumber VARCHAR(1500),
                    filmNumber VARCHAR(1500)
                )
                """
        cursor.execute(create_table_query)

        insert_query = "INSERT INTO customer (name,stateOfIncorporation,street1,street2,city,stateOrCountry,zipCode,accessionNumber,filingDate,reportDate,acceptanceDateTime,form,fileNumber,filmNumber) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_query, (name,stateOfIncorporation,street1,street2,city,stateOrCountry,zipCode,accessionNumber_str,filingDate_str,reportDate_str,acceptanceDateTime_str,form_str,fileNumber_str,filmNumber_str))

        # Commit the transaction
        conn.commit()
                
        # Close the database connection
        cursor.close()
        conn.close()
        return "Successfully stored the data into database"
    
    except Exception as e:
        print(f"Error occured in the database: {e}")
        return None