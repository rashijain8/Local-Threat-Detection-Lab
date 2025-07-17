# Local Threat Detection Lab (LTDL) 🛡️

## Overview
A personal cybersecurity project to simulate and detect local attacks like SSH brute force and port scanning using Python on Linux.

## Structure
- detections/: Python detection scripts
- response/: Auto-blocking IPs
- setup/: VM config and setup
- reports/: For future detection logs
- screenshots/: Screenshots of detection alerts

## Tools Used
- Python
- Ubuntu/Kali Linux
- iptables
- netstat, hydra, nmap

## Sample Attacks
From Kali VM:
nmap -sS <victim-ip>
hydra -l root -P rockyou.txt ssh://<victim-ip>

## Author
rashi jain

