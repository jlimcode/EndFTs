import os
import requests
import io
from image_format import image_to_json

def send_post(upload_string):
    url = 'https://api.web3.storage/upload'
    headers = {'Authorization': "Bearer " + os.getenv("WEB3_STORAGE_API")}
    files = io.BytesIO(bytes(upload_string, encoding='utf-8'))
    files = {'file': io.BufferedReader(raw=files)}
    
    r = requests.post(url, headers=headers, files=files)
    cid = r.json()["cid"]
    base_url = "https://ipfs.io/ipfs/"
    return base_url + cid

def main():
    image_url = "https://i.imgur.com/gYMR2Kk.jpeg"
    url = send_post(image_to_json(image_url))
    print(url)

if __name__ == "__main__":
    main()