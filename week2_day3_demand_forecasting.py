import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv")
df["date"] = pd.to_datetime(df["date"])
product_category = "GROCERY I"
category_data = df[df["family"] == product_category]
daily_demand = category_data.groupby("date")["sales"].sum().reset_index()
daily_demand["forecast"] = daily_demand["sales"].rolling(window=7).mean()
print("Demand Forecasting Model Created Successfully")
print("Product Category:", product_category)
print("\nLast 10 Forecasts:")
print(daily_demand[["date", "sales", "forecast"]].tail(10))
plt.figure(figsize=(12, 6))
plt.plot(daily_demand["date"], daily_demand["sales"], label="Actual Demand")
plt.plot(daily_demand["date"], daily_demand["forecast"], label="7-Day Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Demand Forecasting for GROCERY I")
plt.legend()
plt.tight_layout()
plt.savefig("week2_day3_demand_forecast.png")
plt.show()