Kano SME Phishing Detector:
Protects small businesses in Kano from fake bank alerts (First Bank, GTB, CBN scams).
Problem:
SMEs in Kano receive fake SMS like "Your account blocked, click here".
This leads to account hacking.
How It Works:
Risk scoring system:
No HTTPS: +20
Suspicious keywords (verify, login, account): +15
@ symbol trick: +30
Many hyphens: +10
Long URL: +10
Score:
50+ = PHISHING
20+ = SUSPICIOUS
Below 20 = SAFE
Run:
python phishing_detector.py
Future:
Add Machine Learning
Build web app for traders
Hausa language alert
Author: Najib Muhammad Salis - Northwest University Kano