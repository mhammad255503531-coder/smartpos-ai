import pandas as pd

train = pd.read_csv("train.csv")
stores = pd.read_csv("stores.csv")

print("TRAIN DATASET")
print("Shape:", train.shape)
print("Columns:", list(train.columns))
print("\nFirst 5 rows:")
print(train.head())

print("\nMissing Values:")
print(train.isnull().sum())

print("\nDate Range:")
print("Start:", train["date"].min())
print("End:", train["date"].max())

print("\nUnique Stores:", train["store_nbr"].nunique())
print("Unique Product Families:", train["family"].nunique())

print("\nSales Summary:")
print(train["sales"].describe())

print("\nSTORE DATASET")
print("Shape:", stores.shape)
print("Columns:", list(stores.columns))
print("\nFirst 5 rows:")
print(stores.head())