# Technical Documentation  
Customer Churn Prediction System for E-Commerce

## 1. System Overview
This project implements an end-to-end customer churn prediction system for an e-commerce business using transactional data. The system transforms raw transaction-level data into customer-level features, trains multiple machine learning models, and deploys the best-performing model through an interactive Streamlit web application.

The solution follows industry best practices in data science, including data cleaning, feature engineering, model evaluation, version control, and deployment readiness.

---

## 2. Project Architecture
The project is organized in a modular and scalable structure to ensure maintainability and reproducibility.

- **data/**  
  - raw/: Original dataset and raw data reports  
  - processed/: Cleaned data, engineered features, and JSON artifacts  

- **notebooks/**  
  Jupyter notebooks for data exploration, validation, EDA, and modeling experiments  

- **src/**  
  Python scripts implementing the full data pipeline  
  - Data acquisition  
  - Data cleaning  
  - Feature engineering  
  - Model preparation and training  

- **models/**  
  Serialized trained models and preprocessing objects (scaler, encoders)  

- **app/**  
  Streamlit application for predictions, dashboards, and documentation  

- **docs/**  
  Business understanding, technical documentation, feature dictionary, and reports  

---

## 3. Data Pipeline
### 3.1 Data Acquisition
The dataset is sourced from the UCI Online Retail Dataset, containing over 500,000 transaction records. Data is downloaded and stored in the `data/raw` directory using automated scripts to ensure reproducibility.

### 3.2 Data Cleaning
The cleaning pipeline removes:
- Records with missing CustomerID
- Cancelled invoices
- Negative quantities and invalid prices
- Duplicate transactions
- Statistical outliers using the IQR method  

Derived columns such as total transaction value and time-based attributes are added. Cleaning statistics are saved as structured JSON files for auditability.

### 3.3 Feature Engineering
Transactional data is aggregated to customer-level features, including:
- RFM metrics (Recency, Frequency, Monetary)
- Behavioral patterns
- Temporal activity features
- Product diversity and purchasing preferences  

A temporal split is used to prevent data leakage, and churn is defined based on customer inactivity in a future observation window.

---

## 4. Modeling Approach
Multiple machine learning models are trained and evaluated:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting / XGBoost
- Neural Network

Model selection is based on ROC-AUC, precision, recall, and cross-validation stability. The best-performing model is serialized and stored for deployment.

---

## 5. Deployment Architecture
The trained model is deployed using a Streamlit web application that provides:
- Single customer churn prediction
- Batch predictions via file upload
- Interactive dashboards
- Project documentation  

The application is designed to be lightweight, user-friendly, and suitable for cloud deployment.

---

## 6. Reproducibility and Version Control
- All scripts use relative paths
- Dependencies are listed in `requirements.txt`
- Version control is maintained with frequent, meaningful commits
- Docker configuration is provided for consistent evaluation environments  

---

## 7. Error Handling and Logging
- Logging is implemented in data processing scripts
- Validation checks ensure data integrity at each stage
- JSON artifacts enable automated evaluation and troubleshooting

---

## 8. Assumptions and Limitations
- Churn definition is based on historical inactivity and may not capture intent
- Dataset represents a specific retail period and geography
- Model performance may vary on unseen datasets

---

## 9. Future Enhancements
- Real-time prediction pipeline
- Automated retraining
- Advanced customer segmentation
- Integration with marketing automation tools

---

## 10. Conclusion
This project demonstrates a complete production-ready data science workflow, from raw data ingestion to deployed machine learning application, aligned with real-world business requirements and best practices.
