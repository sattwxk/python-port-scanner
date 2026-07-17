# 🔍 Python Multi-threaded Port Scanner

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)

A fast, multi-threaded TCP port scanner written in Python. It identifies open TCP ports, detects common services, attempts banner grabbing, and exports scan results in TXT and CSV formats.

> ⚠️ **Disclaimer:** This project is intended for educational purposes and authorized security testing only.

---

## ✨ Features

- Multi-threaded TCP Port Scanning
- Interactive Mode
- Command-Line Interface (CLI)
- Hostname Resolution
- Service Detection
- Banner Grabbing
- TXT Report Generation
- CSV Report Generation
- Logging Support
- Thread-safe Output
- Scan Summary

---

## 🛠 Technologies Used

- Python 3
- Socket Programming
- Threading
- argparse
- CSV
- Logging

---

## 📂 Project Structure

```text
python-port-scanner/
│
├── scanner.py
├── port_scanner.py
├── report.py
├── utils.py
│
├── results/
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Requirements

- Python 3.10 or later
- Windows or Linux

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/sattwxk/python-port-scanner.git
```

Enter the project

```bash
cd python-port-scanner
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Interactive Mode

```bash
python scanner.py
```

Example

```text
Enter Target IP / Hostname : 127.0.0.1
Enter Start Port : 1
Enter End Port : 100
```

### Command-Line Mode

Scan localhost

```bash
python scanner.py -t 127.0.0.1 -s 1 -e 1024
```

Scan a hostname

```bash
python scanner.py -t scanme.nmap.org -s 20 -e 100
```

---

## 📊 Example Output

```text
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

## 📄 Reports

Each scan generates:

```text
results/

scan_YYYY-MM-DD_HH-MM-SS.txt
scan_YYYY-MM-DD_HH-MM-SS.csv
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Python Networking
- TCP Socket Programming
- Multi-threading
- File Handling
- Logging
- Command-Line Interfaces
- Report Generation
- Cybersecurity Fundamentals

---

## 🗺️ Roadmap

### Version 1.1

- Colored terminal output
- Progress bar
- JSON report export

### Version 1.2

- SYN Scan using Scapy
- UDP Scanner
- CIDR Network Scanner

### Version 2.0

- GUI
- OS Detection
- CVE Lookup
- Banner Database

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## 👨‍💻 Author

**Sattwik Das**

- GitHub: https://github.com/sattwxk
- LinkedIn: https://linkedin.com/in/sattwikd

---

⭐ If you found this project useful, consider giving it a star on GitHub!