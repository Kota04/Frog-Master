import requests
import json

def scan_file_with_virustotal(file_path):
    api = "1579c2e194f3e92a6670aaf26dd446bd7e2559d832d59057b233a72d09ad5b4b"

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
    size = attributes["size"] * 10**-3  # Convert to KB
    analysis_results = attributes["last_analysis_results"]

    results = []  # List to hold results
    results.append(f"Name: {name}")
    results.append(f"Size: {size:.2f} KB")  # Format size to two decimal places
    results.append(f"Description: {description}")
    results.append(f"SHA-256 Hash: {file_hash}")
    results.append("")  # Blank line for separation

    malicious_count = 0
    for key, values in analysis_results.items():
        verdict = values['category']
        if verdict == 'malicious':
            malicious_count += 1
        results.append(f"{key}: {verdict}")

    if malicious_count:
        results.append(f"\n{malicious_count} antivirus found the given file malicious !!")
    else:
        results.append("\nNo antivirus found the given file malicious !!")

    return results  # Return the list of results
