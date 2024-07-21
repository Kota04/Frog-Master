#!/bin/bash

packet_file="/home/kali/Desktop/MALFROG/BlueSkyRansomware.pcap"

protocols=("http" "smb" "imf" "tftp" "ftp-data" "dicom")

for protocol in "${protocols[@]}"; do
    tshark -r "$packet_file" --export-object "$protocol,/home/kali/Desktop/MALFROG/files"
done
