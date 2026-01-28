# ai-call-analyzer
📞 AI-Powered Call Analyzer

An AI-based Streamlit web application that analyzes phone call conversations to detect spam and fraud calls in real time.
The system uses speech patterns, keywords, and behavioral indicators to alert users about potential scam calls and suggest immediate actions.

🚀 Features

🔊 Real-time Call Analysis (Simulated)

📝 Live Speech-to-Text Transcript

⚠ Fraud Risk Score (0–100%)

🔍 AI Detected Scam Indicators

🚨 Instant User Alerts

❌ End Call / Block / Report Options

🌐 Web-based UI using Streamlit

🧠 How It Works

The system simulates incoming call audio.

Speech is converted into text.

AI analyzes:

Fraud-related keywords (OTP, account block, urgency)

Threatening or pressurizing language

A risk score is generated.

If the risk is high, the user is instantly alerted with reasons.

🛠️ Tech Stack

Frontend & UI: Streamlit (Python)

Programming Language: Python

AI Logic: Rule-based + simulated ML scoring

Deployment: Streamlit Community Cloud

Version Control: GitHub

📂 Project Structure
ai-call-analyzer/
 ├── app.py
 ├── requirements.txt
 └── README.md

⚙️ Installation & Run Locally
1️⃣ Install Dependencies
pip install streamlit

2️⃣ Run the App
python -m streamlit run app.py


The app will open automatically in your browser.

☁️ Deployment

This application is deployed using Streamlit Community Cloud directly from a public GitHub repository.

📸 Output Preview

Call status dashboard

Fraud probability progress bar

Live transcript display

Detected scam reasons

Action buttons (End / Block / Report)
