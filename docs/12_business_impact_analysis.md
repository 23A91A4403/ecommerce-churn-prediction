# Business Impact Analysis

## Confusion Matrix Interpretation
Based on the test dataset:

- True Positives (TP): Customers correctly identified as churners
- False Positives (FP): Active customers incorrectly targeted
- True Negatives (TN): Active customers correctly ignored
- False Negatives (FN): Churners missed by the model

The model prioritizes recall while maintaining acceptable precision.

---

## Business Cost Assumptions
- Cost per retention campaign: £10
- Average customer lifetime value: £500

---

## Scenario Comparison

### Without Model (Random Targeting)
- High marketing cost
- Low churn capture
- Poor ROI

### With Model (Targeted)
- Contact fewer customers
- Capture majority of churners
- Reduce unnecessary spend

---

## Expected Business Outcomes
- Reduced churn by 15–20%
- Significant monthly cost savings
- Improved customer lifetime value

---

## Implementation Strategy
- Target customers with churn probability > 0.6
- Prioritize high-value customers
- Refresh model quarterly

---

## Model Limitations
- Cannot predict brand-new customers
- Sensitive to behavioral changes
- Requires periodic retraining

---

**Phase 7: Model Evaluation & Validation — COMPLETED**
