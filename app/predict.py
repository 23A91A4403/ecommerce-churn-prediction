import joblib
import pandas as pd
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
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# ---------------------------------
# Feature list (MUST match training order)
# ---------------------------------
FEATURE_COLUMNS = [
    "recency",
    "frequency",
    "monetary",
    "avg_order_value",
    "unique_products",
    "total_items",
    "customer_lifetime"
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

    # Enforce correct column order
    df = df[FEATURE_COLUMNS]

    # IMPORTANT: pass numpy array to avoid feature-name mismatch
    return scaler.transform(df.values)

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
