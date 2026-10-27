@"
# Kano SME Phishing Detector

Protects small businesses in Kano from fake bank alerts (First Bank, GTB, CBN scams).

### Problem

SMEs in Kano receive fake SMS like "Your account blocked, click here". This leads to account hacking and loss of business funds.

### How It Works

Risk scoring system:
- No HTTPS: +20
- Suspicious keywords (verify, login, account): +15
- @ symbol trick: +30
- Many hyphens: +10
- Long URL: +10

Score:
- 50+ = PHISHING
- 20+ = SUSPICIOUS
- Below 20 = SAFE

### How to Run

python phishing_detector.py

### Example

Input: http://first-bank-verify.com@login.com
Output: PHISHING (Score: 65)

### Future Improvements

- Add Machine Learning model
- Build web app for traders in Kano
- Add Hausa language alert

**Author:** Najib Muhammad Salis - Northwest University Kano
"@ | Set-Content README.md -Encoding utf8