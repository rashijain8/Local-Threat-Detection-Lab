🧪 Incident Simulation Summary
🧰 Objective
To simulate and detect common network-based threats using Linux tools and Python automation in a local VM lab environment.

💻 Lab Setup
Machine	OS	Role	Tools Used
VM1	Ubuntu 20.04	Victim	Python, netstat, iptables
VM2	Kali Linux	Attacker	nmap, hydra, netcat

Network Mode: Internal/Host-Only

Connectivity: Verified via ping

🔍 Simulated Attacks
SSH brute-force (hydra)

Port scanning (nmap -sS)

Optional: Reverse shell (netcat)

🧠 Detection Methods
Brute force detection via auth.log parsing

Port scan detection via netstat output

Alerts printed to terminal

Auto-block IP using iptables

✅ Results
Threat Type	Detected	Blocked	Detection Script
SSH Brute Force	Yes ✅	Yes ✅	ssh_brute_force.py
Port Scan	Yes ✅	No ❌	port_scan_detect.py

📂 Logs
Raw log: detection-log.txt

Summary: sample-alert-report.md

📅 Date of Simulation
2025-07-17