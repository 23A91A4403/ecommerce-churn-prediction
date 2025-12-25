# Data Dictionary

## Raw Dataset: data.csv

| Column Name | Data Type | Description | Example Values | Missing % | Notes |
|------------|-----------|-------------|----------------|-----------|-------|
| InvoiceNo | String | Invoice number; invoices starting with 'C' indicate cancellations | 536365, C536365 | 0% | Used to identify transactions and cancellations |
| StockCode | String | Product (item) code | 85123A | 0% | Some non-standard and alphanumeric codes exist |
| Description | String | Product description | WHITE HANGING HEART T-LIGHT HOLDER | ~0.27% | Not critical for churn modeling |
| Quantity | Integer | Quantity of each product per transaction | 6, -1 | 0% | Negative values indicate returns |
| InvoiceDate | DateTime | Date and time of transaction | 2010-12-01 08:26:00 | 0% | Date range from 2010 to 2011 |
| UnitPrice | Float | Price per unit in GBP (£) | 2.55 | 0% | Some zero or negative values exist |
| CustomerID | Float | Unique customer identifier | 17850.0 | ~24.9% | High missing rate; required for churn analysis |
| Country | String | Country of customer | United Kingdom | 0% | 38 unique countries |

---

## Data Quality Issues Identified

- High percentage of missing **CustomerID** values (~24.9%)
- Missing product descriptions (~0.27%)
- Cancelled invoices identified by InvoiceNo starting with 'C'
- Negative quantities indicating product returns
- Zero or negative unit prices
- Extremely high quantity values (potential data entry errors)
- Duplicate transaction records

---

## Data Cleaning Required

- Remove rows with missing CustomerID
- Remove cancelled invoices
- Remove rows with negative or zero quantities
- Remove rows with zero or negative prices
- Handle extreme quantity outliers using IQR method
- Convert InvoiceDate to datetime format
- Convert CustomerID to integer after cleaning
- Remove duplicate rows
