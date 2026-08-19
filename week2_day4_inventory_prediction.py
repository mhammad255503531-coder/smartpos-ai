import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv")
df["date"] = pd.to_datetime(df["date"])
product_category = "GROCERY I"
category_data = df[df["family"] == product_category]
daily_sales = category_data.groupby("date")["sales"].sum().reset_index()
recent_sales = daily_sales.tail(30)
average_daily_sales = recent_sales["sales"].mean()
current_inventory = 5000000
days_until_stockout = current_inventory / average_daily_sales
print("Inventory Prediction Results")
print("----------------------------")
print("Product Category:", product_category)
print("Current Inventory:", current_inventory)
print("Average Daily Sales (Last 30 Days):", round(average_daily_sales, 2))
print("Estimated Days Until Stockout:", round(days_until_stockout, 2))
recent_sales["estimated_inventory"] = (
    current_inventory - recent_sales["sales"].cumsum()
)
plt.figure(figsize=(12, 6))
plt.plot(
    recent_sales["date"],
    recent_sales["estimated_inventory"]
)
plt.xlabel("Date")
plt.ylabel("Estimated Remaining Inventory")
plt.title("Inventory Prediction for GROCERY I")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("week2_day4_inventory_prediction.png")
plt.show()