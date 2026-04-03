# 🚀 Simple Network Packet Analyzer (Python + Scapy)

## 📌 Overview
This project is a basic network packet analyzer built using Python and Scapy.  
It captures live TCP traffic and helps visualize how communication happens between systems.

---

## ⚙️ Features
- Capture live TCP packets
- Identify Source IP → Destination IP
- Detect TCP flags (SYN, SYN-ACK, ACK)
- Visualize TCP 3-way handshake
- Map ports to services (HTTP, HTTPS, SSH, DNS)

---

## 🧠 Why I Built This
While learning networking, concepts like the TCP 3-way handshake felt theoretical.  
So I built this tool to actually see how packets move in real time.

---

## ⚠️ Challenges Faced
- Syntax errors while coding
- Logic issues in identifying TCP flags
- Understanding packet structure in Scapy

---

## ✅ What I Learned
- How TCP handshake works in real traffic
- Basics of packet sniffing
- Using Scapy for network analysis
- Debugging real-world issues

---

## 🛠️ Tech Stack
- Python
- Scapy

---

## ▶️ How to Run

```bash
sudo python3 packet_analyzer.py
