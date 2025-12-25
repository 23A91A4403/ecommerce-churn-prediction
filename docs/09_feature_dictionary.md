# Feature Dictionary

## Target Variable

| Feature | Type | Description | Business Meaning |
|------|------|------------|------------------|
| Churn | Binary | 1 = churned, 0 = active | Customer did not purchase in next 3 months |

---

## RFM Features

| Feature | Type | Description | Business Meaning |
|------|------|------------|------------------|
| Recency | Integer | Days since last purchase | Lower = more active |
| Frequency | Integer | Number of purchases | Higher = loyal |
| TotalSpent | Float | Total money spent | Customer value |
| AvgOrderValue | Float | Avg spend per order | Spending behavior |
| UniqueProducts | Integer | Unique products bought | Variety preference |
| TotalItems | Integer | Total items purchased | Purchase volume |

---

## Temporal Features

| Feature | Type | Description |
|------|------|------------|
| CustomerLifetimeDays | Integer | Days between first and last purchase |

---

## Feature Engineering Decisions
- RFM captures customer value and engagement
- Temporal features capture lifecycle behavior
- Churn defined using future inactivity (no leakage)

## Expected Important Features
- Recency (most important)
- Frequency
- TotalSpent
