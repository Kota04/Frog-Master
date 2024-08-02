#!/bin/bash

# File paths
file="CaptureTraffic.pcap"
export_dir="/Files/"
results_file="/Files/analysis_results.txt"
api_key="1579c2e194f3e92a6670aaf26dd446bd7e2559d832d59057b233a72d09ad5b4b"

# Create file and set permissions
touch "$file"
chmod 777 "$file"

# Ensure the export directory exists
if [ ! -d "$export_dir" ]; then
    echo "Export directory $export_dir does not exist. Creating it..."
    mkdir -p "$export_dir"
fi

# Capture traffic
tshark -i wlp0s20f3 -w "$file" -c 1000

# List of protocols to extract
protocols=("http" "smb" "imf" "tftp" "ftp-data" "dicom")

# Extract and export objects for each protocol
for protocol in "${protocols[@]}"; do
    echo "Extracting $protocol objects..."
    # Note: Ensure 'tshark --export-object' is correct for your version
    if ! tshark -r "$file" --export-object "$protocol,$export_dir"; then
        echo "Failed to export $protocol objects."
    fi
done

echo "Traffic capture and export complete."

# Initialize results file
echo "VirusTotal Analysis Results" > "$results_file"
echo "---------------------------" >> "$results_file"

# Analyze files with VirusTotal
for file_path in "$export_dir"*; do
    if [ -f "$file_path" ]; then
        # Compute the MD5 hash of the file content
        file_hash=$(md5sum "$file_path" | awk '{print $1}')
        
        # Query VirusTotal
        response=$(curl -s --request GET \
            --url "https://www.virustotal.com/api/v3/files/$file_hash" \
            --header "x-apikey: $api_key")

        # Write the response to results file
        echo "Results for $(basename "$file_path"):" >> "$results_file"
        echo "$response" >> "$results_file"
        echo "-----------------------------------" >> "$results_file"
    fi
done

echo "VirusTotal analysis complete. Results saved to $results_file."