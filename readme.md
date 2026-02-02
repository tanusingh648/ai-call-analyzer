🧠 AI Call Fraud Detection System
🚨 Problem Statement
Phone fraud and scam calls are increasing rapidly. Users often realize they are being scammed after sharing sensitive information like OTPs or bank details. There is a need for a system that can analyze calls in real time and warn users instantly.

💡 Solution
We built an AI‑powered Call Fraud Detection System that:

Listens to live call audio via microphone

Converts speech to text

Uses a Machine Learning model to detect fraud patterns

Displays real‑time risk alerts on a dashboard

The system works without direct telecom access, making it safe, legal, and practical for real‑world deployment.

🏗️ System Architecture
Phone Call (Speaker Mode)
        ↓
Microphone Capture
        ↓
Speech‑to‑Text
        ↓
ML Fraud Detection Model
        ↓
Risk Score & Alert
        ↓
Web Dashboard
🔧 Tech Stack
Frontend
HTML

CSS

JavaScript (Dashboard UI)

Backend
Python

FastAPI

Uvicorn

AI / ML
SpeechRecognition (Speech‑to‑Text)

scikit‑learn

TF‑IDF Vectorizer

Logistic Regression

Database
SQLite (Call history storage)

🤖 Machine Learning Details
Input: Call transcript text

Vectorization: TF‑IDF (unigrams + bigrams)

Model: Logistic Regression

Output:

Fraud / Safe prediction

Risk score (0–100%)

This approach is lightweight, fast, and explainable — ideal for real‑time analysis.

🎙️ How Call Analysis Works
Due to OS privacy restrictions, apps cannot directly access call audio.
Our system uses a microphone‑based approach:

Call is placed on speaker

Microphone captures audio

Speech is converted to text

ML model analyzes text

Dashboard shows instant alert

This method is widely used in research prototypes and hackathons.

🚀 Features
✅ Live call analysis

✅ Real‑time fraud alerts

✅ Risk score visualization

✅ ML‑based prediction

✅ Call history storage

✅ Works for English & Hinglish

✅ Hackathon‑ready live demo

🖥️ How to Run the Project
1️⃣ Install Dependencies
pip install fastapi uvicorn scikit-learn speechrecognition joblib
2️⃣ Train ML Model
python train_model.py
3️⃣ Start Backend
python -m uvicorn main:app --reload
Backend runs at:

http://127.0.0.1:8000
4️⃣ Open Dashboard
Open index.html in browser and start analyzing calls.

🎤 Hackathon Demo Flow
Put phone call on speaker

Play or speak scam‑like phrases
(“Your bank account is blocked, share OTP”)

Click Analyze Call

Dashboard shows HIGH RISK alert

Explain ML logic to judges

🔮 Future Scope
Android Call Screening integration

Multi‑language fraud detection

Deep learning voice stress analysis

Telecom‑level API integration

Cloud deployment for scale

