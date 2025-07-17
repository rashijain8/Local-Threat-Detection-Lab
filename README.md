🛡️ Local Threat Detection Lab
A lightweight, self-contained cybersecurity lab that simulates and detects common local threats—like brute-force attacks and port scans—using Python scripting and Linux tooling. Designed to foster hands-on learning in detection engineering, infrastructure security, and incident response.

🚀 Features
🔍 Detects brute-force login attempts from log files (e.g., auth.log).

🌐 Identifies port scanning behavior using raw socket capture and logs.

📁 Generates real-time alerts and logs incidents to structured reports.

🤖 Built with automation in mind—simple to run and extend.

🧪 Run entirely in a local Linux environment—no cloud required.

🧠 Why This Project?
This project was created to showcase core competencies aligned with roles like Infrastructure Security Intern or Detection Engineer, including:

Proficiency in Linux environments 🐧

Understanding of TCP/IP, OSI model, and networking concepts 🌐

Security coding in Python 🐍

Detection logic engineering 🛡️

Collaborative documentation & modular code structure 📚

CTF-style experimentation mindset 🎯

📁 Folder Structure
bash
Copy
Edit
Local-Threat-Detection-Lab/
├── detections/            # Brute-force & port scan detection scripts
├── response/              # Alert logging and response automation
├── setup/                 # Environment checker and prerequisites
├── reports/               # Logs, diagrams, and technical report summaries
├── screenshots/           # Screenshots of live execution
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
🔧 Setup & Usage
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/Local-Threat-Detection-Lab.git
cd Local-Threat-Detection-Lab
Run setup script to validate environment:

bash
Copy
Edit
bash setup/environment_check.sh
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run detectors:

Brute-force detector:

bash
Copy
Edit
python detections/brute_force_detector.py
Port scan detector:

bash
Copy
Edit
sudo python detections/port_scan_detector.py
Logs and alerts are saved under:

reports/log_sample.txt

reports/detection_report.md

🖼️ Screenshots
Brute-force Detection	Port Scan Alert

Terminal Execution

📄 Reports
Reports generated include:

Detection Summary: detections of brute-force and scan attempts

Response Log: what was done in reaction to alerts

Architecture Diagram: shows system logic

Sample Log Files: real-time outputs

See the full reports under the reports/ folder:

reports/detection_report.md

reports/response_report.md

🧩 Technologies Used
Python 3

Linux OS (Tested on Ubuntu)

Bash Scripting

Raw Sockets & Log Parsing

Markdown & Diagrams
