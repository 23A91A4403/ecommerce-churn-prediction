# EDA Key Insights

## 1. Churn Patterns Discovered

1. Recency is the strongest churn indicator  
2. Churned customers have much higher recency values  
3. Frequency is significantly lower for churned customers  
4. High-spending customers churn less  
5. Customer lifetime strongly correlates with churn  
6. Purchase velocity is lower for churned users  
7. Low-frequency segment has highest churn rate  
8. High-frequency customers rarely churn  
9. Correlation heatmap confirms Recency dominance  
10. RFM features clearly separate churned vs active users  

Statistical tests confirm multiple features with p < 0.05.

---

## 2. Customer Segment Analysis

- Low-frequency customers show highest churn  
- Medium-frequency customers are moderate risk  
- High-frequency customers are most loyal  

Segment-based retention strategies are recommended.

---

## 3. Feature Recommendations for Modeling

Recommended features:
- Recency
- Frequency
- TotalSpent
- CustomerLifetimeDays
- PurchaseVelocity

These features show strong statistical and visual separation.

---

## 4. Hypotheses for Modeling

H1: Customers with Recency > 90 days are significantly more likely to churn  
H2: High-frequency customers (>10 purchases) rarely churn  
H3: Long customer lifetime reduces churn probability  

These hypotheses will guide model selection and feature importance analysis.
