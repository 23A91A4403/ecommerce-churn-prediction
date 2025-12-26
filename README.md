# E-Commerce Customer Churn Prediction

## Project Overview
Customer churn is a critical challenge for e-commerce businesses, as losing existing customers directly impacts revenue and long-term growth. Retaining customers is often more cost-effective than acquiring new ones, making churn prediction an important business problem.

This project implements an end-to-end machine learning solution to predict whether a customer is likely to stop purchasing within the next three months. The pipeline includes data acquisition, cleaning, feature engineering, model training, evaluation, and deployment. The final solution is deployed as a live Streamlit web application that allows stakeholders to make real-time churn predictions.

---

## Business Problem
E-commerce companies invest significant resources in acquiring customers. However, customer churn leads to revenue loss and reduced customer lifetime value. Identifying customers who are likely to churn in advance enables businesses to take proactive retention actions such as personalized offers, loyalty programs, and targeted marketing campaigns.

**Objective:**  
To identify high-risk customers early and support data-driven customer retention strategies.

---

## Dataset
- **Source:** UCI Online Retail Dataset (via Kaggle)  
- **URL:** https://www.kaggle.com/datasets/carrie1/ecommerce-data  
- **Size:** 541,909 rows × 8 columns  
- **Period:** December 2010 – December 2011  

After preprocessing:
- **392,692 cleaned transactions**
- **4,372 unique customers**

---

## Methodology

### 1. Data Cleaning
- Removed cancelled invoices
- Handled missing CustomerID values
- Removed invalid quantities and prices
- Eliminated duplicate records
- Removed outliers to reduce noise

### 2. Feature Engineering
- Aggregated transaction-level data to customer-level data
- Created RFM features (Recency, Frequency, Monetary)
- Added behavioral features (items purchased, product diversity)
- Added temporal features (customer lifetime, activity duration)
- Defined churn using an inactivity-based time window

### 3. Models Evaluated

| Model               | ROC-AUC | Precision | Recall |
|--------------------|--------:|----------:|-------:|
| Logistic Regression | 0.68 | 0.65 | 0.61 |
| Decision Tree       | 0.70 | 0.67 | 0.64 |
| Random Forest       | 0.73 | 0.71 | 0.66 |
| Gradient Boosting   | **0.75** | **0.74** | **0.69** |

### 4. Final Model
- **Selected Model:** Gradient Boosting Classifier  
- **Performance:** ROC-AUC 0.75, Precision 0.74, Recall 0.69, F1-score 0.71  

The Gradient Boosting model provided the best balance between predictive performance and generalization.

---

## Installation & Usage
# Clone repository
git clone https://github.com/23A91A4403/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app/streamlit_app.py


### Local Setup

#### Clone Repository
```bash
git clone https://github.com/23A91A4403/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction
```


### Live Application

### URL:https://ecommerce-churn-prediction-3nwr22bnvx9mwus6wcp562.streamlit.app/

#### Project Structure
ecommerce-churn-prediction/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── 01_data_acquisition.py
│   ├── 02_data_cleaning.py
│   ├── 03_feature_engineering.py
│   └── 04_model_preparation.py
    └── test_model.py
├── notebooks/
│   ├── 01_initial_data_exploration.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_feature_eda.ipynb
│   ├── 04_baseline_model.ipynb
│   ├── 05_advanced_models.ipynb
│   ├── 06_model_evaluation.ipynb
│   └── 07_cross_validation.ipynb
├── models/
│   ├── baseline_metrics.json
│   ├── best_model.pkl
│   └── scaler.pkl
├── app/
│   ├── streamlit_app.py
│   └── predict.py
├── docs/
│   ├── [All documentation files]
├── visualizations/
│   ├── related images
├── requirements.txt
├── .gitignore
├──  README.md
├──  Dockerfile
├── Docker-compose.yml
├── presentation.pdf
├── submission.json

---

## Results
- Achieved a **ROC-AUC score of 0.75**, meeting the required performance threshold.
- Precision and recall values demonstrate effective identification of churned customers.
- Cross-validation results indicate stable and consistent model performance.
- Feature importance analysis highlights recency, frequency, and monetary value as strong churn indicators.

---

## Business Impact
- Enables early identification of customers likely to churn.
- Supports targeted retention strategies such as personalized discounts and loyalty programs.
- Helps marketing teams optimize campaign spending by focusing on high-risk customers.
- Reduces revenue loss and improves customer lifetime value.
- Provides a scalable and deployable solution suitable for real-world business use.

---
