# Data Cleaning Strategy

## 1. Missing Values Strategy

### CustomerID (Missing: ~24.9%)
**Decision:** DROP  

**Reasoning:**  
CustomerID is essential for creating customer-level features such as Recency,
Frequency, Monetary (RFM), and churn labels. Rows without CustomerID cannot be
associated with any customer and therefore cannot be used for churn prediction.

**Impact:**  
Approximately 135,080 rows will be removed.

---

### Description (Missing: ~0.27%)
**Decision:** KEEP  

**Reasoning:**  
Product description is not required for churn prediction. Missing values in
Description do not affect transaction counts, monetary value, or temporal
features used for modeling.

---

## 2. Handling Cancellations

**Issue:**  
Invoices starting with the letter **'C'** represent cancelled transactions.

**Strategy Options:**  
- Option A: Remove all cancellations  
- Option B: Retain cancellations as features  

**Chosen Strategy:** Option A – Remove all cancellations  

**Reasoning:**  
Cancelled invoices do not represent completed purchases. Including them would
negatively impact revenue, frequency, and monetary feature calculations.

---

## 3. Negative Quantities

**Issue:**  
Negative quantities indicate returned products.

**Strategy:**  
Remove all rows where **Quantity ≤ 0**.

**Reasoning:**  
Returns do not represent positive customer purchasing behavior and distort
transaction frequency and monetary value metrics.

---

## 4. Outliers

### Quantity Outliers
**Detection Method:** Interquartile Range (IQR)  

**Threshold:**  
Values below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR  

**Action:** Remove extreme outliers  

**Reasoning:**  
Extremely high quantities likely result from data entry errors or bulk purchases
that are not representative of typical customer behavior.

---

### Price Outliers
**Strategy:**  
Remove rows where **UnitPrice ≤ 0**.

**Reasoning:**  
Zero or negative prices are invalid and corrupt revenue-based feature
calculations.

---

## 5. Data Type Conversions

- **InvoiceDate:** Converted to datetime format  
- **CustomerID:** Converted to integer after removing missing values  
- **Quantity:** Integer  
- **UnitPrice:** Float (already numeric)  

---

## 6. Duplicate Handling

**Strategy:**  
Remove exact duplicate rows across all columns.

**Reasoning:**  
Duplicate records artificially inflate transaction counts and revenue values,
leading to incorrect customer behavior modeling.

---

## Summary

The data cleaning process focuses on improving data reliability, ensuring
accurate customer-level feature generation, and maintaining a realistic data
retention rate of approximately **60–70%**, as required by the project
guidelines.
