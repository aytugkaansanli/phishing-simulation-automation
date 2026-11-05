# Enterprise Phishing Simulation & Automation Framework

This repository contains the infrastructure configuration, mail security protocols, and Python automation scripts used for conducting corporate cybersecurity awareness and phishing simulations.

## 🚀 Technologies & Tools Used
* **Infrastructure:** Linux (Ubuntu) Cloud VPS, SSH Port Hardening
* **Simulation Framework:** Gophish
* **Mail Security & Protocols:** SMTP Relay, SPF, DKIM, DMARC
* **Automation:** Python (Requests API Integration)

## 📌 Project Architecture
1. **Server Setup & Hardening:** Deployed on a remote Linux cloud instance with customized administrative ports.
2. **Mail Deliverability Configuration:** Configured dedicated SMTP routing and implemented DNS-level email authentication (SPF, DKIM, DMARC) to simulate realistic threat vectors without hitting spam flags.
3. **Simulation & Metrics:** Managed targeted social engineering campaigns to assess human-risk factors and internal security awareness.
4. **Python Automation:** Utilized Python scripts to interact with the Gophish REST API for campaign tracking and data extraction.
