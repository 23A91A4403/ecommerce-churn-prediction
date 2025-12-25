import pandas as pd
import pickle

# Load processed features (inside container)
df = pd.read_csv("/app/data/processed/data_features.csv")

# Load saved model (inside container)
with open("/app/data/processed/rf_model.pkl", "rb") as f:
    clf = pickle.load(f)

# Take first 5 rows as example
X = df[['Recency', 'Frequency', 'Monetary', 'AvgPurchaseValue']].head()

# Make predictions
preds = clf.predict(X)
print("Predictions for first 5 customers:", preds)
