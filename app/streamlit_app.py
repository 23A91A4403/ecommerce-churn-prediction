import streamlit as st
import pandas as pd
import plotly.express as px
from predict import predict, predict_proba

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Single Prediction", "Batch Prediction", "Model Dashboard", "Documentation"]
)

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "Home":
    st.title("Customer Churn Prediction System")
    st.write("""
    This web application predicts whether a customer is likely to churn
    (stop purchasing in the next 3 months) based on historical behavior.
    """)
    st.success("Model: Gradient Boosting | ROC-AUC > 0.75")

# -----------------------------
# SINGLE PREDICTION
# -----------------------------
elif page == "Single Prediction":
    st.header("Single Customer Prediction")

    col1, col2 = st.columns(2)

    with col1:
        recency = st.number_input("Days Since Last Purchase", 0, 500)
        frequency = st.number_input("Number of Purchases", 1, 200)
        monetary = st.number_input("Total Amount Spent (£)", 0.0)
        avg_order = st.number_input("Average Order Value (£)", 0.0)

    with col2:
        unique_products = st.number_input("Unique Products Purchased", 1, 500)
        total_items = st.number_input("Total Items Purchased", 1, 5000)
        lifetime = st.number_input("Customer Lifetime (days)", 1, 2000)

    if st.button("Predict Churn Risk"):
        input_data = {
            "recency": recency,
            "frequency": frequency,
            "monetary": monetary,
            "avg_order_value": avg_order,
            "unique_products": unique_products,
            "total_items": total_items,
            "customer_lifetime": lifetime
        }

        prob = predict_proba(input_data)[0]
        label = predict(input_data)[0]

        st.subheader("Prediction Result")
        st.write(f"**Churn Probability:** {prob:.2f}")
        st.write("**Prediction:**", "Churned" if label == 1 else "Active")

        if prob > 0.7:
            st.error("High risk – Immediate retention action recommended")
        elif prob > 0.4:
            st.warning("Medium risk – Engagement recommended")
        else:
            st.success("Low risk – Customer likely to stay")

# -----------------------------
# BATCH PREDICTION
# -----------------------------
elif page == "Batch Prediction":
    st.header("Batch Prediction")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if file:
        try:
            df = pd.read_csv(file)

            probs = predict_proba(df)
            preds = predict(df)

            df["Churn_Probability"] = probs
            df["Churn_Prediction"] = preds

            st.success("Predictions completed")
            st.dataframe(df.head())

            st.download_button(
                "Download Results",
                df.to_csv(index=False),
                "churn_predictions.csv"
            )
        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------------
# MODEL DASHBOARD
# -----------------------------
elif page == "Model Dashboard":
    st.header("Model Performance Dashboard")

    try:
        comparison = pd.read_csv("models/model_comparison.csv")
        fig = px.bar(
            comparison,
            x="Model",
            y="ROC_AUC",
            title="Model ROC-AUC Comparison"
        )
        st.plotly_chart(fig)
    except:
        st.warning("Model comparison file not available")

# -----------------------------
# DOCUMENTATION
# -----------------------------
elif page == "Documentation":
    st.header("Documentation")
    st.write("""
    - Input features are customer-level RFM and behavioral metrics
    - Model predicts churn risk for the next 90 days
    - Use batch prediction for targeted marketing campaigns
    """)
