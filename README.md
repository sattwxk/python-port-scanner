# 🔍 Python Multi-threaded Port Scanner

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)

A fast, multi-threaded TCP port scanner written in Python. This tool identifies open ports, detects common services, attempts banner grabbing, and generates TXT and CSV reports.

> ⚠️ This project is intended for **educational purposes and authorized security testing only**.

---

# Features

- Multi-threaded TCP Port Scanning
- Service Detection
- Banner Grabbing
- Hostname Resolution
- TXT Report Generation
- CSV Report Generation
- Logging Support
- Command Line Interface
- Thread-safe Output
- Scan Summary

---

# Technologies Used

- Python 3
- Socket Library
- Threading
- Argparse
- CSV
- Logging

---

# Project Structure

```
Port Scanner/
│
├── scanner.py
├── port_scanner.py
├── report.py
├── utils.py
│
├── docs/
│   └── screenshots/
│
├── results/
├── tests/
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/sattwxk/python-port-scanner.git
```

Enter the project directory

```bash
cd python-port-scanner
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Scan localhost

```bash
python scanner.py -t 127.0.0.1 -s 1 -e 1024
```

Scan a hostname

```bash
python scanner.py -t scanme.nmap.org -s 20 -e 100
```

---

# Example Output

```
============================================================
Python Multi-threaded Port Scanner
============================================================

Target : scanme.nmap.org

============================================================
Port : 22
Service : ssh
Banner : OpenSSH

============================================================
Port : 80
Service : http
Banner : Apache

============================================================
Scan Summary

Open Ports : 2

Time Taken : 0:00:01.72
============================================================
```

---

# Reports

Every scan automatically generates

```
results/

scan_2026-07-09_18-42-20.txt

scan_2026-07-09_18-42-20.csv
```

TXT Report

```
Port : 22
Service : ssh
Banner : OpenSSH

---------------------------------

Port : 80
Service : http
Banner : Apache
```

CSV Report

```
Port,Service,Banner
22,ssh,OpenSSH
80,http,Apache
```

---


# Future Improvements

- SYN Scan using Scapy
- UDP Scanner
- CIDR Network Scanner
- OS Detection
- Banner Database
- JSON Report Export
- Progress Bar
- Colored Output
- REST API
- GUI Version

---

# Learning Objectives

This project demonstrates

- Python Networking
- TCP Socket Programming
- Threading
- File Handling
- Logging
- Command Line Interfaces
- Cybersecurity Fundamentals
- Report Generation

---

# Disclaimer

This software is intended for educational purposes and authorized penetration testing only.

Do not scan systems that you do not own or have explicit permission to test.

The author is not responsible for misuse of this software.

---

# License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

# Author

**Sattwik Das**
Linkedin : https://linkedin.com/in/sattwikd
GitHub: https://github.com/sattwxk

Version 1.1
-----------
✓ Colored Output

✓ Progress Bar

✓ JSON Export

Version 1.2
-----------
✓ SYN Scan

✓ UDP Scan

✓ CIDR Scanner

Version 2.0
-----------
✓ GUI

✓ OS Detection

✓ CVE Lookup

✓ Banner Database