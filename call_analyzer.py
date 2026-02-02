from live_listener import listen_once
from ml_predictor import predict

def analyze_call():
    text = listen_once()
    if not text:
        return {"prediction": "UNKNOWN", "risk": 0}

    result = predict(text)
    return {
        "text": text,
        "prediction": result["prediction"],
        "risk": result["risk"]
    }
