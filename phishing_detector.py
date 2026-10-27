# Kano SME Phishing Detector
# Protects small businesses from fake bank links
# Author: Najib Muhammad Salis - Northwest University Kano

def check_url(url):
    """Check if a URL is phishing and give risk score"""
    score = 0
    reasons = []
    
    # Convert to small letters for easy checking
    low_url = url.lower()
    
    # Rule 1: No HTTPS = 20 points risk
    if not low_url.startswith("https://"):
        score += 20
        reasons.append("No HTTPS (not secure)")
    
    # Rule 2: Suspicious keywords = 15 points each
    suspicious_words = ["secure", "verify", "login", "account", "firstbankk", "gtb-secure", "update", "confirm"]
    for word in suspicious_words:
        if word in low_url:
            score += 15
            reasons.append(f"Suspicious keyword: '{word}'")
    
    # Rule 3: @ symbol trick (phishing uses @) = 30 points
    if "@" in url:
        score += 30
        reasons.append("Contains @ symbol (phishing trick)")
    
    # Rule 4: Many hyphens (-) = 10 points
    if url.count("-") >= 3:
        score += 10
        reasons.append("Too many hyphens (-)")
    
    # Rule 5: Too long URL = 10 points
    if len(url) > 75:
        score += 10
        reasons.append("URL is too long")
    
    # Final result
    if score >= 50:
        result = "🚨 PHISHING"
    elif score >= 20:
        result = "⚠️  SUSPICIOUS"
    else:
        result = "✅ SAFE"
    
    return result, score, reasons

# --- Demo for Kano SMEs ---
print("=== Kano SME Phishing Detector ===\n")

test_links = [
    "https://www.firstbanknigeria.com",
    "http://firstbankk-secure-verify.com/login",
    "https://gtbank.com",
    "http://gtb-secure-update-account.com@fake.com/login",
    "https://www.cbn.gov.ng"
]

for link in test_links:
    result, score, reasons = check_url(link)
    print(f"Link: {link}")
    print(f"Result: {result} - Risk {score}%")
    if reasons:
        print(f"Reasons: {', '.join(reasons)}")
    print("-" * 60)