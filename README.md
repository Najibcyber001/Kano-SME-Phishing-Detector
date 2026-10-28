# Kano SME Phishing Detector

A lightweight Python tool to protect Small and Medium Enterprises in Kano, Nigeria from phishing attacks.

## Problem
SMEs in Kano lose money daily to fake bank alerts, fraudulent supplier invoices, and phishing links via WhatsApp and SMS.

## Solution
This tool scans URLs and email content using rule-based detection to flag suspicious patterns.

## Features
- Detects fake domains and typosquatting
- Checks for suspicious keywords (urgent, verify account, blocked)
- Flags URL shorteners and IP-based links
- Simple CLI for non-technical staff

## How to Run
\\\ash
python phishing_detector.py --url https://example.com
\\\

## Tech Stack
- Python 3.x
- Regex and URL parsing

## Author
**Najib Muhammad Salis** - Cybersecurity Student, Northwest University Kano | Aspiring SOC Analyst
