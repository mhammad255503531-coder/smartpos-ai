import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train_featured.csv")

df["date"] = pd.to_datetime(df["date"])

daily_sales = df.groupby("date")["sales"].sum()

moving_average = daily_sales.rolling(window=7).mean()

print("Daily Sales:")
print(daily_sales.head())

print("\n7-Day Moving Average:")
print(moving_average.head(15))

plt.figure(figsize=(12, 6))

plt.plot(daily_sales, label="Daily Sales")
plt.plot(moving_average, label="7-Day Moving Average")

plt.title("Daily Sales and 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()

plt.tight_layout()
plt.savefig("moving_average_forecast.png")

print("\nMoving average chart saved as: moving_average_forecast.png")