#!/bin/bash

packet_file=""/home/kota/Frog-Master/CaptureTraffic.pcap"

protocols=("http" "smb" "imf" "tftp" "ftp-data" "dicom")

for protocol in "${protocols[@]}"; do
    tshark -r "$packet_file" --export-object "$protocol,/home/kota/Frog-Master/files"
done
