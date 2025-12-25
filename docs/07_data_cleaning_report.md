# Data Cleaning Report

## Overview
This report documents the data cleaning steps applied to the raw e-commerce transaction dataset (`data.csv`) as part of Phase 3: Data Cleaning.  
The goal of this phase was to improve data quality while retaining a sufficient amount of data for reliable churn modeling.

---

## Dataset Summary

- **Original Rows:** 541,909  
- **Rows After Cleaning:** 333,234  
- **Rows Removed:** 208,675  
- **Retention Rate:** 61.49%  

This retention rate falls within the expected range (60–70%) specified in the project requirements.

---

## Cleaning Steps Applied

### 1. Handling Missing CustomerID
- **Issue:** CustomerID is missing for ~24.9% of rows.
- **Action Taken:** Rows with missing `CustomerID` were removed.
- **Reason:** Customer-level churn modeling requires a valid customer identifier.
- **Impact:** Largest reduction in dataset size.

---

### 2. Handling Invalid Transactions
- **Issue:**  
  - Negative or zero `Quantity` values (returns/cancellations)  
  - Zero or negative `UnitPrice` values
- **Action Taken:** Rows where `Quantity <= 0` or `UnitPrice <= 0` were removed.
- **Reason:** These transactions do not represent valid purchases and can distort revenue-based features.

---

### 3. Duplicate Records
- **Issue:** Duplicate transaction rows present in the dataset.
- **Action Taken:** Duplicate rows were removed using exact row matching.
- **Reason:** Prevents double-counting transactions and customers.

---

### 4. Data Type Corrections
- **InvoiceDate:** Converted to `datetime` format for temporal analysis.
- **CustomerID:** Converted to integer after removing missing values.
- **UnitPrice & Quantity:** Retained as numeric values.

---

## Data Quality Validation

After cleaning:
- No missing values remain in critical columns.
- All quantities are positive.
- All prices are positive.
- CustomerID values are valid integers.
- Date range remains intact (2010–2011).

Validation results were saved to:
- `data/processed/validation_report.json`

---

## Output Artifacts Generated

- `data/processed/cleaned_transactions.csv`
- `data/processed/cleaning_statistics.json`
- `data/processed/validation_report.json`

---

## Conclusion

The dataset is now clean, consistent, and suitable for:
- Customer-level aggregation
- Feature engineering (RFM metrics)
- Churn modeling

Phase 3 (Data Cleaning & Validation) is successfully completed.
