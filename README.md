# Evil Twin Attack Simulation with ELK Monitoring

This project demonstrates an **Evil Twin Wi-Fi attack** in a controlled lab environment. It simulates the process of setting up a rogue access point (Fake AP) to trick users into connecting, captures test credentials through a fake login portal, and uses the **ELK Stack (Elasticsearch, Logstash, Kibana)** to monitor logs in real time.

>  **Disclaimer:** This project is for educational and research purposes only. It must only be used in isolated environments with full authorization. Never deploy this on public networks or against real users.

---

##  Architecture Overview

```plaintext
Victim Device
     |
     | (1) Connects
     v
Fake Access Point (airbase-ng)
     |
     | (2) DHCP via dnsmasq
     v
Captive Portal (Apache2)
     |
     | (3) Submits credentials
     v
Logger (creds.txt)
     |
     | (4) Logstash parses logs
     v
Elasticsearch stores data
     |
     | (5) Kibana displays analytics
```
##  Components Used
airbase-ng – Create rogue Wi-Fi AP

dnsmasq – Handle DHCP/DNS requests

Apache2 – Serve a fake login portal (HTML/PHP)

Logstash – Parse credential logs

Elasticsearch – Store structured logs

Kibana – Visualize captured data
