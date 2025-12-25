import pandas as pd
import numpy as np
from datetime import timedelta
import json

# Paths
INPUT_PATH = "data/processed/cleaned_transactions.csv"
OUTPUT_PATH = "data/processed/customer_features.csv"

print("Loading cleaned transactions...")
df = pd.read_csv(INPUT_PATH, parse_dates=["InvoiceDate"])

# -----------------------------
# STEP 1: Define time windows
# -----------------------------
max_date = df["InvoiceDate"].max()
training_cutoff = max_date - timedelta(days=90)

train_df = df[df["InvoiceDate"] <= training_cutoff]
obs_df = df[df["InvoiceDate"] > training_cutoff]

# -----------------------------
# STEP 2: Define churn
# -----------------------------
train_customers = set(train_df["CustomerID"].unique())
obs_customers = set(obs_df["CustomerID"].unique())

customers = pd.DataFrame({"CustomerID": list(train_customers)})
customers["Churn"] = customers["CustomerID"].apply(
    lambda x: 1 if x not in obs_customers else 0
)

print("Churn rate:", customers["Churn"].mean() * 100)

# -----------------------------
# STEP 3: RFM FEATURES
# -----------------------------
rfm = train_df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (training_cutoff - x.max()).days),
    Frequency=("InvoiceNo", "nunique"),
    TotalSpent=("TotalPrice", "sum"),
    AvgOrderValue=("TotalPrice", "mean"),
    UniqueProducts=("StockCode", "nunique"),
    TotalItems=("Quantity", "sum")
).reset_index()

customers = customers.merge(rfm, on="CustomerID", how="left")

# -----------------------------
# STEP 4: TEMPORAL FEATURES
# -----------------------------
lifetime = train_df.groupby("CustomerID").agg(
    FirstPurchase=("InvoiceDate", "min"),
    LastPurchase=("InvoiceDate", "max")
).reset_index()

lifetime["CustomerLifetimeDays"] = (
    lifetime["LastPurchase"] - lifetime["FirstPurchase"]
).dt.days

customers = customers.merge(
    lifetime[["CustomerID", "CustomerLifetimeDays"]],
    on="CustomerID",
    how="left"
)

# -----------------------------
# STEP 5: SAVE OUTPUT
# -----------------------------
customers.to_csv(OUTPUT_PATH, index=False)

feature_info = {
    "total_customers": len(customers),
    "total_features": len(customers.columns) - 2,
    "churn_rate": float(customers["Churn"].mean()),
    "features": list(customers.columns)
}

with open("data/processed/feature_info.json", "w") as f:
    json.dump(feature_info, f, indent=4)

print("Feature engineering completed successfully!")
print("Saved customer features to:", OUTPUT_PATH)
