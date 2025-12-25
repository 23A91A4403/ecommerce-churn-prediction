import joblib
import pandas as pd
import numpy as np
import os

# ---------------------------------
# Get absolute path to project root
# ---------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "gradient_boosting.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

# ---------------------------------
# Load model and scaler
# ---------------------------------
def load_model():
    return joblib.load(MODEL_PATH)

def load_scaler():
    return joblib.load(SCALER_PATH)

model = load_model()
scaler = load_scaler()

# ---------------------------------
# Preprocess input
# ---------------------------------
def preprocess_input(data):
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise ValueError("Input must be dict or DataFrame")

    return scaler.transform(df)

# ---------------------------------
# Predict churn label
# ---------------------------------
def predict(data):
    X = preprocess_input(data)
    return model.predict(X)

# ---------------------------------
# Predict churn probability
# ---------------------------------
def predict_proba(data):
    X = preprocess_input(data)
    return model.predict_proba(X)[:, 1]
