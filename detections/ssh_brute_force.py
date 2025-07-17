# detections/ssh_brute_force.py

import re
from collections import defaultdict

log_file = "/var/log/auth.log"
ip_counter = defaultdict(int)
threshold = 5

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                ip_counter[ip] += 1

for ip, count in ip_counter.items():
    if count >= threshold:
        print(f"[ALERT] SSH brute force detected from {ip} ({count} attempts)")
