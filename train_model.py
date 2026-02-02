from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Training data
texts = [
    "please share your otp urgently",
    "your bank account is suspended",
    "verify your kyc now",
    "tell me your password",
    "your card has been blocked",
    "hello how are you",
    "let us meet tomorrow",
    "your order has been delivered",
    "thank you for calling",
    "happy birthday"
]

labels = [1,1,1,1,1, 0,0,0,0,0]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Save model
joblib.dump(model, "fraud_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ ML model trained & saved")
texts += [
  "apna otp bataye",
  "aapka bank khata band ho jayega",
  "turant verify kijiye",
  "kyc complete karo"
]
labels += [1,1,1,1]
recognize_google(audio, language="hi-IN")
