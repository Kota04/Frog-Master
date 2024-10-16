#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file="$1"
export_dir="./files"
api_key="1579c2e194f3e92a6670aaf26dd446bd7e2559d832d59057b233a72d09ad5b4b"

chmod 777 "$file"
[ -d "$export_dir" ] && rm -rf "$export_dir"/* || mkdir "$export_dir"

protocols=("http" "smb" "imf" "tftp" "ftp-data" "dicom")

for protocol in "${protocols[@]}"; do
    tshark -r "$file" --export-object "$protocol,$export_dir" || 
    echo "Failed to export $protocol objects."
done

for f in "$export_dir"/*; do
    
    [[ "$f" == *.txt ]] && rm "$f" && continue
    base_name=$(basename "$f" | sed 's/([0-9])//g')
    base_path="$export_dir/$base_name"

    if [ -f "$base_path" ] && [ "$f" != "$base_path" ]; then
        rm -v "$f"
    elif [ "$f" != "$base_path" ]; then
        mv -v "$f" "$base_path"
    fi
done

echo "Duplicate removal complete."
