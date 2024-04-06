import requests

def file_download():

    print("Downloading starting")

    # url1 = 'https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip'

    url2 = 'https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip'

    req = requests.get(url2)
    
    filename = url2.split('/')[-1]
    if req.status_code == 200:
        with open(filename,'wb') as output_file:
            output_file.write(req.content)
        print('Downloading Completed')
    else:
        print(f"Failed to download '{url2}'. Status code: {req.status_code}")