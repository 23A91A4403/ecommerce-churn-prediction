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

### Local Setup

#### Clone Repository
```bash
git clone https://github.com/23A91A4403/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction
