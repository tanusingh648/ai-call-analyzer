import random

KEYWORDS = {
    "OTP": 15,
    "Bank Account": 20,
    "KYC": 12,
    "Urgent": 10,
    "Verify Now": 14
}

BEHAVIORS = [
    "Scripted Speech",
    "Emotional Pressure",
    "High Urgency Tone",
    "Sensitive Info Request",
    "Caller Interrupting"
]

def analyze_call():
    keyword = random.choice(list(KEYWORDS.keys()))
    behavior = random.choice(BEHAVIORS)

    return {
        "keyword": keyword,
        "behavior": behavior,
        "risk": KEYWORDS[keyword]
    }
