touch CaptureTraffic.pcap

chmod 777 CaptureTraffic.pcap

tshark -i wlp0s20f3 -w CaptureTraffic.pcap