# Technical Approach

## Classification Approach
Customer churn is a binary outcome (churned or active), making this a classification problem
rather than regression. Classification models are suitable for predicting discrete outcomes
and evaluating performance using metrics such as ROC-AUC, Precision, and Recall.

## Feature Engineering
Customer-level features will be engineered from transaction data, including:
- RFM metrics (Recency, Frequency, Monetary)
- Behavioral features (purchase patterns)
- Temporal features (recent activity windows)

## Model Strategy
Multiple machine learning algorithms will be tested to compare performance:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- Neural Network

The best-performing model will be selected based on validation metrics.

## Deployment Strategy
The final model will be deployed using a Streamlit web application and packaged using Docker
to ensure reproducibility and consistent evaluation.
