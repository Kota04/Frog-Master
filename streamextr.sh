#!/bin/bash

PCAP_FILE="/home/kali/Desktop/MALFROG/BlueSkyRansomware.pcap"

# Extract TCP conversation details
tshark -r "$PCAP_FILE" -q -z conv,tcp > conv_details.txt

# Check if the conversation details file is not empty
if [ ! -s conv_details.txt ]; then
  echo "No TCP conversations found in the PCAP file."
  exit 1
fi

# Extract stream indices from conversation details
awk '/<->/ {print NR-4}' conv_details.txt | grep -Eo '[0-9]+' > comb.txt

# Check if the stream indices file is not empty
if [ ! -s comb.txt ]; then
  echo "No stream indices found in the conversation details."
  exit 1
fi

# Extract ASCII data for each stream index
while read -r stream_index; do
  echo "Extracting stream index $stream_index..."
  tshark -r "$PCAP_FILE" -q -z follow,tcp,ascii,$stream_index > "stream_$stream_index.txt"
done < comb.txt

echo "Extraction complete."
