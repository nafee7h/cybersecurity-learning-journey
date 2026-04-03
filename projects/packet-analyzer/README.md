# 🚀 Network Packet Analyzer (Python + Scapy)

## 📌 Overview
This project is a basic network packet analyzer built using Python and Scapy.
It captures live TCP traffic and helps visualize communication between systems.

## ⚙️ Features
- Capture live TCP packets
- Identify Source IP → Destination IP
- Detect TCP flags (SYN, SYN-ACK, ACK)
- Visualize TCP 3-way handshake
- Map ports to services (HTTP, HTTPS, SSH, DNS)

## 📸 Sample Output
[SYN] 10.0.2.15 → 142.251.220.14 | 35836 → http  
[SYN-ACK] 142.251.220.14 → 10.0.2.15 | 80 → Unknown  
[ACK] 10.0.2.15 → 142.251.220.14 | 35836 → http  

## 🧠 Why I Built This
I wanted to move beyond theory and observe real packet flow,
especially how SYN, SYN-ACK, and ACK packets appear in real network communication.

## ⚠️ Challenges Faced
- Syntax errors while coding  
- Logic issues in identifying TCP flags  
- Understanding packet structure in Scapy  

## ✅ What I Learned
- How TCP handshake works in real traffic  
- Basics of packet sniffing  
- Using Scapy for network analysis  
- Debugging real-world issues  

## 🛠️ Tech Stack
- Python  
- Scapy  

## 📦 Requirements
pip install scapy

## ▶️ How to Run
sudo python3 packet_analyzer.py

## 📌 Note
This is a beginner-level project and part of my cybersecurity learning journey.
