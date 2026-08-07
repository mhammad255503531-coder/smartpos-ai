import pandas as pd

df = pd.read_csv("train.csv")

print("Original Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

df["date"] = pd.to_datetime(df["date"])

df = df.dropna()

df = df[df["sales"] >= 0]
df = df[df["onpromotion"] >= 0]
df = df[df["store_nbr"].between(1, 54)]

print("\nCleaned Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.to_csv("train_cleaned.csv", index=False)

print("\nCleaned dataset saved as: train_cleaned.csv")