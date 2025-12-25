import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import json
import os

# Paths
INPUT_PATH = "data/processed/customer_features.csv"
OUTPUT_DIR = "data/processed"
MODEL_DIR = "models"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

print("Loading customer features...")
df = pd.read_csv(INPUT_PATH)

# ----------------------------
# STEP 1: Separate target
# ----------------------------
y = df["Churn"]
X = df.drop(columns=["Churn", "CustomerID"])

# ----------------------------
# STEP 2: Train / Val / Test split
# ----------------------------
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, stratify=y_temp, random_state=42
)

# ----------------------------
# STEP 3: Scale numerical features
# ----------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# ----------------------------
# STEP 4: Save outputs
# ----------------------------
pd.DataFrame(X_train_scaled, columns=X.columns).to_csv(f"{OUTPUT_DIR}/X_train.csv", index=False)
pd.DataFrame(X_val_scaled, columns=X.columns).to_csv(f"{OUTPUT_DIR}/X_val.csv", index=False)
pd.DataFrame(X_test_scaled, columns=X.columns).to_csv(f"{OUTPUT_DIR}/X_test.csv", index=False)

y_train.to_csv(f"{OUTPUT_DIR}/y_train.csv", index=False)
y_val.to_csv(f"{OUTPUT_DIR}/y_val.csv", index=False)
y_test.to_csv(f"{OUTPUT_DIR}/y_test.csv", index=False)

joblib.dump(scaler, f"{MODEL_DIR}/scaler.pkl")

with open(f"{OUTPUT_DIR}/feature_names.json", "w") as f:
    json.dump(list(X.columns), f, indent=4)

print("✅ Data Preparation Completed")
print(f"Train size: {len(X_train)}")
print(f"Validation size: {len(X_val)}")
print(f"Test size: {len(X_test)}")
print(f"Churn rate train: {y_train.mean()*100:.2f}%")
print(f"Churn rate test: {y_test.mean()*100:.2f}%")
