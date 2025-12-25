# Business Problem Statement

## 1. Business Context
The e-commerce industry is highly competitive, and customer retention is a critical challenge.
Acquiring new customers is significantly more expensive than retaining existing ones, with costs
estimated to be 5–25 times higher. RetailCo Analytics aims to improve customer retention by
leveraging historical transaction data to understand customer behavior.

Currently, the business lacks a data-driven approach to identify customers who are likely to stop
purchasing, resulting in ineffective marketing campaigns and lost revenue.

## 2. Problem Definition
Customer churn is defined as:
**A customer who has not made a purchase in the last 90 days.**

The objective is to predict which customers are likely to churn in the next 3 months.

## 3. Stakeholders
- **Marketing Team:** Requires customer segmentation and churn predictions to run targeted retention campaigns.
- **Sales Team:** Needs insights into high-risk customers to prioritize outreach.
- **Product Team:** Needs purchasing pattern insights for personalized offers.
- **Executive Team:** Requires ROI projections and business impact analysis.

## 4. Business Impact
- Expected reduction in churn rate by **15–20%**
- Increased customer lifetime value through targeted retention
- Reduced marketing costs by focusing only on high-risk customers

## 5. Success Metrics
Primary Metric:
- **ROC-AUC Score > 0.78**

Secondary Metrics:
- Precision > 0.75 (minimize false positives)
- Recall > 0.70 (identify actual churners)
- F1-Score > 0.72
