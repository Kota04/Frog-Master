import requests
import json
import sys

def scan_file_with_virustotal(file_path):
    api = "1579c2e194f3e92a6670aaf26dd446bd7e2559d832d59057b233a72d09ad5b4b"
    file_path

    file_to_upload = {"file": open(file_path, "rb")}
    url = r'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {"apikey": api}
    response = requests.post(url, files=file_to_upload, params=params)

    file_url = f"https://www.virustotal.com/api/v3/files/{response.json()['sha1']}"
    headers = {"accept": "application/json", "x-apikey": api}

    print("Analysing...")
    response = requests.get(file_url, headers=headers)
    report = json.loads(response.text)

    attributes = report["data"]["attributes"]
    name = attributes.get("meaningful_name", "unable to fetch")
    file_hash = attributes["sha256"]
    description = attributes["type_description"]
    size = attributes["size"] * 10**-3
    analysis_results = attributes["last_analysis_results"]

    print(f"Name: {name}")
    print(f"Size: {size} KB")
    print(f"Description: {description}")
    print(f"SHA-256 Hash: {file_hash}")
    print()

    malicious_count = 0
    for key, values in analysis_results.items():
        verdict = values['category']
        if verdict == 'malicious':
            malicious_count += 1
        print(f"{key}: {verdict}")

    if malicious_count:
        print(f"\n{malicious_count} antivirus found the given file malicious !!")
    else:
        print("\nNo antivirus found the given file malicious !!")

