import pandas as pd
import joblib

MODEL_PATH = "models/gradient_boosting.pkl"
SCALER_PATH = "models/scaler.pkl"

FEATURE_COLUMNS = [
    "Recency",
    "Frequency",
    "TotalSpent",
    "AvgOrderValue",
    "UniqueProducts",
    "TotalItems",
    "CustomerLifetimeDays"
]

# ---------------------------
# Load model
# ---------------------------
def load_model():
    return joblib.load(MODEL_PATH)

# ---------------------------
# Load scaler
# ---------------------------
def load_scaler():
    return joblib.load(SCALER_PATH)

# ---------------------------
# Preprocess input
# ---------------------------
def preprocess_input(data):
    """
    Accepts dict (single) or DataFrame (batch)
    Returns scaled DataFrame
    """
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise ValueError("Input must be dict or DataFrame")

    # Ensure required columns
    missing = set(FEATURE_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing features: {missing}")

    df = df[FEATURE_COLUMNS]

    scaler = load_scaler()
    df_scaled = scaler.transform(df)

    return df_scaled

# ---------------------------
# Predict churn label
# ---------------------------
def predict(data):
    model = load_model()
    X = preprocess_input(data)
    return model.predict(X)

# ---------------------------
# Predict churn probability
# ---------------------------
def predict_proba(data):
    model = load_model()
    X = preprocess_input(data)
    return model.predict_proba(X)[:, 1]
