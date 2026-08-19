import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
df = pd.read_csv("train.csv")
df["date"] = pd.to_datetime(df["date"])
product_category = "GROCERY I"
df = df[df["family"] == product_category].copy()
df = df.groupby("date", as_index=False).agg({
    "sales": "sum",
    "onpromotion": "sum"
})
df["lag_1"] = df["sales"].shift(1)
df["lag_7"] = df["sales"].shift(7)
df["rolling_mean_7"] = df["sales"].shift(1).rolling(window=7).mean()
df = df.dropna()
X = df[["lag_1", "lag_7", "rolling_mean_7", "onpromotion"]]
y = df["sales"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions) ** 0.5
mae = mean_absolute_error(y_test, predictions)
print("Week 2 Day 5: Feature Improvements")
print("-----------------------------------")
print("Product Category:", product_category)
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print("RMSE:", round(rmse, 2))
print("MAE:", round(mae, 2))