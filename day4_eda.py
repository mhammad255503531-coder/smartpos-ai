import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train_cleaned.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

sales_by_date = df.groupby("date")["sales"].sum()

print("\nSales by Date:")
print(sales_by_date.head())

print("\nTotal Days:")
print(sales_by_date.shape[0])

plt.figure(figsize=(12, 6))
plt.plot(sales_by_date.index, sales_by_date.values)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sales_by_family = df.groupby("family")["sales"].sum().sort_values(ascending=False)

print("\nTop 10 Best-Selling Product Families:")
print(sales_by_family.head(10))

top_10 = sales_by_family.head(10)

plt.figure(figsize=(10, 6))
top_10.plot(kind="bar")
plt.title("Top 10 Best-Selling Product Families")
plt.xlabel("Product Family")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()