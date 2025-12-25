import pandas as pd
import os
from datetime import datetime

RAW_PATH = "data/raw/data.csv"
PROFILE_PATH = "data/raw/data_profile.txt"

def download_dataset():
    """
    Load dataset from local CSV file (Kaggle download)
    """
    os.makedirs("data/raw", exist_ok=True)

    df = pd.read_csv(RAW_PATH, encoding="latin1")

    print("Dataset loaded successfully")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print(f"Timestamp: {datetime.now()}")

    return True


def load_raw_data():
    df = pd.read_csv(RAW_PATH, encoding="latin1")
    return df


def generate_data_profile(df):
    with open(PROFILE_PATH, "w") as f:
        f.write(f"Rows: {df.shape[0]}\n")
        f.write(f"Columns: {df.shape[1]}\n\n")
        f.write("Column Names & Types:\n")
        f.write(str(df.dtypes))
        f.write("\n\nMemory Usage:\n")
        f.write(str(df.memory_usage(deep=True)))
        f.write("\n\nPreview:\n")
        f.write(str(df.head()))

    print("Data profile generated successfully")


if __name__ == "__main__":
    download_dataset()
    df = load_raw_data()
    generate_data_profile(df)
