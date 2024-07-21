import os
import hashlib
import virustotal_python
from pprint import pprint

# Directory containing the files
directory_path = "/home/kali/Desktop/MALFROG/files"

# VirusTotal API key
API_KEY = "1579c2e194f3e92a6670aaf26dd446bd7e2559d832d59057b233a72d09ad5b4b"

# Initialize VirusTotal API
with virustotal_python.Virustotal(API_KEY) as vtotal:
    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            # Compute the MD5 hash of the file content
            with open(file_path, "rb") as file:
                file_content = file.read()
                file_hash = hashlib.md5(file_content).hexdigest()
            
            # Query VirusTotal with the computed MD5 hash
            try:
                resp = vtotal.request(f"files/{file_hash}")
                print(f"Results for {filename}:")
                pprint(resp.data)
            except Exception as e:
                print(f"An error occurred for {filename}: {e}")
