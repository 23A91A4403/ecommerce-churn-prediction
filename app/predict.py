import joblib
import pandas as pd
import numpy as np

# -----------------------------
# Load model and scaler
# -----------------------------
def load_model():
    return joblib.load("../models/gradient_boosting.pkl")

def load_scaler():
    return joblib.load("../models/scaler.pkl")

model = load_model()
scaler = load_scaler()

# -----------------------------
# Preprocess input
# -----------------------------
def preprocess_input(data):
    """
    Accepts:
    - dict (single customer)
    - DataFrame (batch)
    Returns scaled DataFrame
    """
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise ValueError("Invalid input format")

    df_scaled = scaler.transform(df)
    return df_scaled

# -----------------------------
# Predict churn label
# -----------------------------
def predict(data):
    X = preprocess_input(data)
    return model.predict(X)

# -----------------------------
# Predict churn probability
# -----------------------------
def predict_proba(data):
    X = preprocess_input(data)
    return model.predict_proba(X)[:, 1]
