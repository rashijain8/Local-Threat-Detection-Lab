📊 Threat Detection Report
1️⃣ SSH Brute Force Detection
Detection Script: ssh_brute_force.py

Source IP: 192.168.1.4

Attempts: 7

Status: ✅ Detected

Action Taken: 🔐 IP blocked using iptables

2️⃣ Port Scan Detection
Detection Script: port_scan_detect.py

Scan Type: SYN scan (nmap -sS)

Open Ports Found: 12

Status: ✅ Detected

Action Taken: ❌ No block (monitor-only)

3️⃣ Response Summary
Total Alerts: 2

IPs Blocked: 1

Logs Saved: Yes (see detection-log.txt)

📅 Timestamp
Date & Time: 2025-07-17 14:32