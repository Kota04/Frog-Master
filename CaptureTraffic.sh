#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "filters and interface should be sent"
    exit 1
fi

file="CaptureTraffic.pcap"
export_dir="./files"
api_key="1579c2e194f3e92a6670aaf26dd446bd7e2559d832d59057b233a72d09ad5b4b"

touch "$file" && chmod 777 "$file"
[ -d "$export_dir" ] && rm -rf "$export_dir"/* || mkdir "$export_dir"

tshark -i $1 $2 -w "$file" -c 1000

protocols=("http" "smb" "imf" "tftp" "ftp-data" "dicom")

for protocol in "${protocols[@]}"; do
    tshark -r "$file" --export-object "$protocol,$export_dir"
done

for file in "$export_dir"/*; do
    [[ "$file" == *.txt ]] && rm "$file" && continue
    

    
    base_name=$(basename "$file" | sed 's/([0-9])//g')
    base_path="$export_dir/$base_name"
    
    [ -f "$base_path" ] && [ "$file" != "$base_path" ] && rm "$file" || mv "$file" "$base_path"
done
