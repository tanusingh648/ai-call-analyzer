KEYWORDS = {
    "otp": 20,
    "bank": 18,
    "account": 15,
    "kyc": 12,
    "urgent": 10,
    "verify": 14,
    "password": 25
}

def analyze_text(text):
    text = text.lower()
    risk = 0
    detected = []

    for word, score in KEYWORDS.items():
        if word in text:
            detected.append(word)
            risk += score

    return {
        "risk": min(risk, 100),
        "keywords": detected
    }
