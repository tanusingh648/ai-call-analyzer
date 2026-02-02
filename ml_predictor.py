import joblib

model = joblib.load("fraud_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict(text):
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0][1]

    return {
        "prediction": "FRAUD" if prob > 0.6 else "SAFE",
        "risk": int(prob * 100)
    }
