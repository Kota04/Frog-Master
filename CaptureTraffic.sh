#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "filters and interface should be sent"
    exit 1
fi

# File paths
file="CaptureTraffic.pcap"
export_dir="./files"  
results_file="./analysis_results.txt" 
api_key="1579c2e194f3e92a6670aaf26dd446bd7e2559d832d59057b233a72d09ad5b4b"

current_directory=$(pwd)

# Create file and set permissions
touch "$file"
chmod 777 "$file"

# Ensure the export directory exists and is empty
if [ -d "$export_dir" ]; then
    echo "Emptying folder: $export_dir"
    rm -rf "$export_dir"/*  # Correctly targets files within the export directory
else
    echo "Creating folder: $export_dir"
    mkdir "$export_dir"
fi

# Capture traffic
tshark -i $1 $2 -w "$file" -c 1000

# List of protocols to extract
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

# Remove duplicate files by comparing base filenames and suffixes
echo "Removing duplicate files..."

for file in "$export_dir"/*; do
    # Extract the base name of the file (e.g., 'del.ps1' from 'del(1).ps1')
    base_name=$(echo "$(basename "$file")" | sed 's/([0-9])//g')
    base_path="$export_dir/$base_name"
    
    # If a file with the base name already exists, remove the current file
    if [ -f "$base_path" ] && [ "$file" != "$base_path" ]; then
        echo "Removing duplicate file: $file"
        rm -v "$file"
    else
        # Rename the current file to its base name if it's not already done
        if [ "$file" != "$base_path" ]; then
            mv -v "$file" "$base_path"
        fi
    fi
done

echo "Duplicate removal complete."