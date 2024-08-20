import requests
import json
import sys

def write_to_json_file(filename: str, content: dict):
    with open(filename, 'w') as file:
        json.dump(content, file, indent=4)

def upload_file_to_virustotal(file_path: str, api_key: str) -> dict:
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {"apikey": api_key}
    try:
        with open(file_path, "rb") as file:
            response = requests.post(url, files={"file": file}, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        write_to_json_file("output.json", {"error": f"Failed to upload file: {e}"})
        sys.exit(1)

def get_analysis_report(sha1: str, api_key: str) -> dict:
    file_url = f"https://www.virustotal.com/api/v3/files/{sha1}"
    headers = {"accept": "application/json", "x-apikey": api_key}
    try:
        response = requests.get(file_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        write_to_json_file("output.json", {"error": f"Failed to retrieve analysis report: {e}"})
        sys.exit(1)

def main():
    api_key = "1579c2e194f3e92a6670aaf26dd446bd7e2559d832d59057b233a72d09ad5b4b"
    file_path = "./files/javaw.exe"
    
    # Upload file and get SHA-1 hash from the response
    upload_response = upload_file_to_virustotal(file_path, api_key)
    write_to_json_file("output.json", {"Upload Response": upload_response})
    
    sha1 = upload_response.get("sha1")
    
    if not sha1:
        write_to_json_file("output.json", {"error": "Failed to retrieve SHA-1 hash from the upload response."})
        sys.exit(1)

    # Get and display the analysis report
    report = get_analysis_report(sha1, api_key)
    write_to_json_file("output.json", {"Analysis Report": report})

if __name__ == "__main__":
    main()
