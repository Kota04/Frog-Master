#!/bin/bash

# File paths
file="CaptureTraffic.pcap"
export_dir="./files"
touch "$file"
# Set file permissions
chmod 777 "$file"

# Capture traffic
tshark -i wlp0s20f3 -w "$file" -c 50

# List of protocols to extract
protocols=("http" "smb" "imf" "tftp" "ftp-data" "dicom")

# Extract and export objects for each protocol
for protocol in "${protocols[@]}"; do
    tshark -r "$file" --export-object "$protocol,$export_dir"
done
