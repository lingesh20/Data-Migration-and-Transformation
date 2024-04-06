import zipfile

def extract_file():

    # Specify the path to your zip file
    zip_file_path = 'C:/Users/linge/OneDrive/Documents/capstone2/submissions.zip'

    # Specify the directory where you want to extract the contents
    extract_path = 'C:/Users/linge/OneDrive/Documents/capstone2/files/'

    # Open the zip file in read mode
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(extract_path)

    print(f"Contents of '{zip_file_path}' successfully extracted to '{extract_path}'.")
