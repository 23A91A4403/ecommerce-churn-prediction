import pandas as pd
import json
import os

# =========================
# PATHS
# =========================
RAW_DATA_PATH = "data/raw/data.csv"
CLEAN_DATA_PATH = "data/processed/cleaned_transactions.csv"
STATS_PATH = "data/processed/cleaning_statistics.json"

os.makedirs("data/processed", exist_ok=True)

# =========================
# LOAD RAW DATA
# =========================
df = pd.read_csv(RAW_DATA_PATH, encoding="ISO-8859-1")

original_rows = len(df)

# =========================
# DATA CLEANING STEPS
# =========================

# 1. Remove missing CustomerID
df = df.dropna(subset=["CustomerID"])

# 2. Remove cancelled invoices (InvoiceNo starts with 'C')
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# 3. Remove missing descriptions
df = df.dropna(subset=["Description"])

# 4. Remove negative or zero Quantity and UnitPrice
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# 5. Remove duplicate rows
df = df.drop_duplicates()

# 6. Convert data types
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["CustomerID"] = df["CustomerID"].astype(int)

# =========================
# OUTLIER REMOVAL (IQR)
# =========================

# Quantity outliers
Q1 = df["Quantity"].quantile(0.25)
Q3 = df["Quantity"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["Quantity"] >= Q1 - 1.5 * IQR) & (df["Quantity"] <= Q3 + 1.5 * IQR)]

# UnitPrice outliers
Q1 = df["UnitPrice"].quantile(0.25)
Q3 = df["UnitPrice"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["UnitPrice"] >= Q1 - 1.5 * IQR) & (df["UnitPrice"] <= Q3 + 1.5 * IQR)]

# =========================
# FEATURE ENRICHMENT
# =========================
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["DayOfWeek"] = df["InvoiceDate"].dt.dayofweek
df["Hour"] = df["InvoiceDate"].dt.hour

# =========================
# SAVE CLEANED DATA
# =========================
df.to_csv(CLEAN_DATA_PATH, index=False)

# =========================
# CLEANING STATISTICS
# =========================
final_rows = len(df)

cleaning_statistics = {
    "original_rows": original_rows,
    "rows_after_cleaning": final_rows,
    "rows_removed": original_rows - final_rows,
    "retention_rate": round((final_rows / original_rows) * 100, 2),
    "cleaning_steps": [
        "Removed missing CustomerID",
        "Removed cancelled invoices",
        "Removed missing descriptions",
        "Removed negative quantities and prices",
        "Removed duplicates",
        "Removed outliers using IQR",
        "Converted data types",
        "Added derived time features"
    ]
}

with open(STATS_PATH, "w") as f:
    json.dump(cleaning_statistics, f, indent=4)

# =========================
# DONE
# =========================
print("✅ Data Cleaning Completed Successfully")
print(f"Original rows: {original_rows}")
print(f"Rows after cleaning: {final_rows}")
print(f"Retention rate: {cleaning_statistics['retention_rate']}%")
print(f"Saved cleaned data to: {CLEAN_DATA_PATH}")
print(f"Saved statistics to: {STATS_PATH}")
