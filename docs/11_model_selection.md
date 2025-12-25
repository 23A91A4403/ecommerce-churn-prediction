# Model Selection Report

## Objective
The objective of this phase is to select the best-performing churn prediction model based on quantitative evaluation metrics and business suitability. Multiple machine learning models were trained and compared using the same feature set and validation strategy to ensure fair comparison.

---

## Models Evaluated
The following models were implemented and evaluated:

1. Logistic Regression (Baseline)
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. Neural Network (MLP)

All models were trained using the same customer-level features and evaluated on a held-out validation set using ROC-AUC as the primary metric.

---

## Evaluation Metric
**Primary Metric:** ROC-AUC  

ROC-AUC was chosen because:
- It measures the model’s ability to distinguish between churned and active customers
- It is robust to class imbalance
- It aligns with business needs for ranking customers by churn risk

---

## Model Performance Summary

| Model | ROC-AUC |
|------|--------|
| Logistic Regression | Baseline |
| Decision Tree | Moderate |
| Random Forest | High |
| Gradient Boosting | Highest |
| Neural Network | High |

Exact performance values are stored in `models/model_comparison.csv`.

---

## Selected Model
**Gradient Boosting Classifier** was selected as the final model.

---

## Justification for Model Selection

### 1. Predictive Performance
- Gradient Boosting achieved the highest ROC-AUC score among all evaluated models
- Demonstrates strong separation between churned and active customers

### 2. Generalization Ability
- Performs well on unseen validation data
- Less prone to overfitting compared to Decision Trees and Neural Networks

### 3. Interpretability vs Performance Balance
- More interpretable than Neural Networks
- Provides feature importance scores useful for business insights

### 4. Business Suitability
- Enables accurate ranking of customers by churn probability
- Suitable for targeted retention campaigns
- Stable and production-ready

---

## Rejected Models – Rationale

- **Logistic Regression:** Too simplistic with lower predictive power
- **Decision Tree:** Overfitting risk and instability
- **Random Forest:** Strong performance but slightly inferior to Gradient Boosting
- **Neural Network:** Less interpretable and harder to tune

---

## Final Decision
The **Gradient Boosting model** is selected as the final churn prediction model for deployment.

It provides the best balance between:
- Predictive accuracy
- Stability
- Interpretability
- Business usability

---

## Next Steps
- Perform final evaluation on the test dataset
- Save and version the selected model
- Deploy the model via Streamlit for churn prediction

---

**Phase 6: Model Development & Selection — COMPLETED**
