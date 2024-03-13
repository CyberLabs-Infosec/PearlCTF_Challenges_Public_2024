# WiFi Broken

Here a pcap file is given which contains deauth and EAPOL packets.

EAPOL packet can easily be bruteforced using aircrack-ng

```python
sudo aircrack-ng -w ~/rockyou.txt findme.cap
```

Flag: pearl{shenoydx}
