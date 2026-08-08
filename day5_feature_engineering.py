import pandas as pd

df = pd.read_csv("train_cleaned.csv")

df["date"] = pd.to_datetime(df["date"])

df["day_of_week"] = df["date"].dt.dayofweek
df["month"] = df["date"].dt.month
df["day_of_year"] = df["date"].dt.dayofyear
df["year"] = df["date"].dt.year

df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)

print("Dataset Shape:")
print(df.shape)

print("\nNew Features:")
print(df[[
    "date",
    "day_of_week",
    "month",
    "day_of_year",
    "year",
    "is_weekend"
]].head(10))

df.to_csv("train_featured.csv", index=False)

print("\nFeature-engineered dataset saved as: train_featured.csv")