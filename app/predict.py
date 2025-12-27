import joblib
import pandas as pd
import os

# ---------------------------------
# Paths
# ---------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "gradient_boosting.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

# ---------------------------------
# Load model and scaler
# ---------------------------------
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# ---------------------------------
# EXACT features used during training
# (DO NOT change order or names)
# ---------------------------------
FEATURE_COLUMNS = [
    "CustomerID",
    "Recency",
    "Frequency",
    "TotalSpent",
    "AvgOrderValue",
    "UniqueProducts",
    "TotalItems",
    "CustomerLifetimeDays"
]

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

    # If CustomerID is missing, add dummy value
    if "CustomerID" not in df.columns:
        df["CustomerID"] = 0

    # Ensure correct column order
    df = df[FEATURE_COLUMNS]

    # IMPORTANT: use NumPy array to avoid sklearn feature-name issues
    X = scaler.transform(df.to_numpy())

    return X

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
