import streamlit as st
import pandas as pd
import plotly.express as px
from predict import predict, predict_proba

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Single Prediction", "Batch Prediction", "Documentation"]
)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":
    st.title("Customer Churn Prediction System")
    st.write(
        "This application predicts whether a customer is likely to churn "
        "in the next 3 months using historical transaction behavior."
    )
    st.success("Model: Gradient Boosting | ROC-AUC ≥ 0.75")

# -----------------------------
# SINGLE PREDICTION
# -----------------------------
elif page == "Single Prediction":
    st.header("Single Customer Prediction")

    col1, col2 = st.columns(2)

    with col1:
        recency = st.number_input("Days Since Last Purchase", min_value=0)
        frequency = st.number_input("Number of Purchases", min_value=1)
        total_spent = st.number_input("Total Amount Spent (£)", min_value=0.0)
        avg_order = st.number_input("Average Order Value (£)", min_value=0.0)

    with col2:
        unique_products = st.number_input("Unique Products Purchased", min_value=1)
        total_items = st.number_input("Total Items Purchased", min_value=1)
        lifetime = st.number_input("Customer Lifetime (days)", min_value=1)

    if st.button("Predict Churn Risk"):
        input_data = {
            "CustomerID": 0,  # dummy ID for single prediction
            "Recency": recency,
            "Frequency": frequency,
            "TotalSpent": total_spent,
            "AvgOrderValue": avg_order,
            "UniqueProducts": unique_products,
            "TotalItems": total_items,
            "CustomerLifetimeDays": lifetime
        }

        prob = predict_proba(input_data)[0]
        label = predict(input_data)[0]

        st.subheader("Prediction Result")
        st.write(f"**Churn Probability:** {prob:.2f}")
        st.write("**Prediction:**", "Churned" if label == 1 else "Active")

        if prob >= 0.7:
            st.error("High risk – Immediate retention action recommended")
        elif prob >= 0.4:
            st.warning("Medium risk – Engagement recommended")
        else:
            st.success("Low risk – Customer likely to stay")

# -----------------------------
# BATCH PREDICTION
# -----------------------------
elif page == "Batch Prediction":
    st.header("Batch Prediction")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if file is not None:
        try:
            try:
                df = pd.read_csv(file, encoding="utf-8")
            except UnicodeDecodeError:
                df = pd.read_csv(file, encoding="latin1")

            probs = predict_proba(df)
            preds = predict(df)

            df["Churn_Probability"] = probs
            df["Churn_Prediction"] = preds

            st.success("Predictions completed successfully")
            st.dataframe(df.head())

            st.download_button(
                "Download Results",
                df.to_csv(index=False),
                file_name="churn_predictions.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error(str(e))


# -----------------------------
# DOCUMENTATION
# -----------------------------
elif page == "Documentation":
    st.header("Documentation")
    st.write(
        """
        - Features are customer-level RFM and behavioral metrics  
        - Churn is defined as 90 days of inactivity  
        - The model outputs churn probability and label  
        - Use batch prediction for marketing campaigns  
        """
    )
