import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
df = pd.read_csv("train.csv")
df["date"] = pd.to_datetime(df["date"])
df = df[["date", "store_nbr", "family", "sales", "onpromotion"]]
df = pd.get_dummies(df, columns=["family"], drop_first=True)
X = df.drop(columns=["sales", "date"])
y = df["sales"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions) ** 0.5
mae = mean_absolute_error(y_test, predictions)
print("Model Evaluation Results")
print("------------------------")
print("RMSE:", rmse)
print("MAE:", mae)
plt.figure(figsize=(10, 6))
plt.scatter(y_test[:1000], predictions[:1000], alpha=0.5)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.tight_layout()
plt.savefig("week2_day2_actual_vs_predicted.png")
plt.show()