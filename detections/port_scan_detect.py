# detections/port_scan_detect.py

import subprocess

output = subprocess.getoutput("netstat -ntu")
lines = output.split("\n")[2:]
ports = [line.split()[3].split(":")[-1] for line in lines if ":" in line]

if len(set(ports)) > 10:
    print("[ALERT] Unusual number of open ports — possible port scan")
