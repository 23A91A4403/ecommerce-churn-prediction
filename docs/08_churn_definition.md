# Churn Definition

## Problem Statement
We need to identify customers who are likely to stop purchasing from the e-commerce platform.

## Approach: Observation Window Method

### Total Data Period
- Start Date: 2010-12-01
- End Date: 2011-12-09

### Time Split
- **Training Period:** From start date up to 90 days before the last transaction
- **Observation Period:** Last 90 days of data

### Churn Definition
A customer is considered **CHURNED** if:
- The customer made at least one purchase in the training period, AND
- The customer made zero purchases in the observation period (next 3 months)

A customer is considered **ACTIVE** if:
- The customer made at least one purchase in the training period, AND
- The customer made at least one purchase in the observation period

### Justification
- A 3-month window is an industry standard for e-commerce churn
- It balances seasonal effects and customer inactivity
- Aligns with quarterly business planning

### Validation Rules
- Expected churn rate: 20%–40%
- No data leakage: features only from training period
- Clear time separation between features and target
Note:
The observed churn rate (~43%) is slightly above the expected range.
This is acceptable due to dataset sparsity and strict 90-day inactivity definition.

