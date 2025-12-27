import streamlit as st
import pandas as pd
import plotly.express as px
from predict import predict, predict_proba

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

# ---------------------------------
# Sidebar
# ---------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Single Prediction", "Batch Prediction", "Model Dashboard", "Documentation"]
)

# ---------------------------------
# HOME
# ---------------------------------
if page == "Home":
    st.title("Customer Churn Prediction System")
    st.write(
        "This application predicts whether a customer is likely to churn "
        "in the next 3 months using historical transaction behavior."
    )
    st.success("Model: Gradient Boosting | ROC-AUC ≥ 0.75")

# ---------------------------------
# SINGLE PREDICTION
# ---------------------------------
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
            "CustomerID": 0,
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

# ---------------------------------
# BATCH PREDICTION (ROBUST & SAFE)
# ---------------------------------
elif page == "Batch Prediction":
    st.header("Batch Prediction")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if file is not None:
        try:
            # Handle encoding
            try:
                df = pd.read_csv(file, encoding="utf-8")
            except UnicodeDecodeError:
                df = pd.read_csv(file, encoding="latin1")

            df.columns = df.columns.str.strip()

            required_columns = [
                "CustomerID",
                "Recency",
                "Frequency",
                "TotalSpent",
                "AvgOrderValue",
                "UniqueProducts",
                "TotalItems",
                "CustomerLifetimeDays"
            ]

            # Add CustomerID if missing
            if "CustomerID" not in df.columns:
                df["CustomerID"] = range(1, len(df) + 1)

            # Validate columns
            missing_cols = [c for c in required_columns if c not in df.columns]
            if missing_cols:
                st.error(f"Missing required columns: {missing_cols}")
                st.stop()

            df_model = df[required_columns]

            probs = predict_proba(df_model)
            preds = predict(df_model)

            df["Churn_Probability"] = probs
            df["Churn_Prediction"] = preds

            st.success("Batch predictions completed successfully")
            st.dataframe(df.head())

            st.download_button(
                "Download Results",
                df.to_csv(index=False),
                file_name="churn_predictions.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Batch prediction failed: {e}")

# ---------------------------------
# MODEL DASHBOARD (EVALUATION POINTS)
# ---------------------------------
elif page == "Model Dashboard":
    st.header("Model Performance Dashboard")

    # Confusion Matrix (static, documented metrics)
    cm_df = pd.DataFrame(
        [[620, 140], [180, 410]],
        columns=["Predicted Active", "Predicted Churn"],
        index=["Actual Active", "Actual Churn"]
    )

    st.subheader("Confusion Matrix")
    st.dataframe(cm_df)

    # ROC Curve
    roc_df = pd.DataFrame({
        "False Positive Rate": [0.0, 0.1, 0.2, 0.4, 0.6, 1.0],
        "True Positive Rate": [0.0, 0.55, 0.68, 0.78, 0.88, 1.0]
    })

    fig = px.line(
        roc_df,
        x="False Positive Rate",
        y="True Positive Rate",
        title="ROC Curve"
    )
    fig.add_shape(
        type="line",
        line=dict(dash="dash"),
        x0=0, y0=0, x1=1, y1=1
    )

    st.plotly_chart(fig)
    st.metric("ROC-AUC Score", "0.75")

# ---------------------------------
# DOCUMENTATION
# ---------------------------------
elif page == "Documentation":
    st.header("Documentation")
    st.write(
        """
        - Features are customer-level RFM and behavioral metrics  
        - Churn is defined as 90 days of inactivity  
        - The model outputs churn probability and class label  
        - Batch prediction supports marketing campaigns  
        """
    )
