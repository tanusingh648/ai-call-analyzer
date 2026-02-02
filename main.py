from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (perfect for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend running ✅"}

@app.get("/analyze")
def analyze():
    return {
        "detected_keyword": "OTP",
        "behavior": "Asking Sensitive Info",
        "risk_increase": 15
    }

@app.get("/live-call")
def live_call():
    return {
        "text": "Please share your OTP",
        "risk": 75,
        "prediction": "FRAUD"
    }
