# response/block_ip.py

import os

def block_ip(ip):
    command = f"sudo iptables -A INPUT -s {ip} -j DROP"
    os.system(command)
    print(f"[ACTION] Blocked IP: {ip}")

block_ip("192.168.1.5")  # Replace with real IP
