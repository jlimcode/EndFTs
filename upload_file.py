import os
import requests
import json

def send_post(upload_file):
    url = 'https://api.web3.storage/upload'
    headers = {'Authorization': os.getenv("WEB3_STORAGE_API")}
    files = {'file': open(upload_file, 'rb')}

    requests.post(url, headers=headers, files=files)