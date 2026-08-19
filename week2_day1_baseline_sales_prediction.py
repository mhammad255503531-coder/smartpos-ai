import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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
print("Baseline Sales Prediction Model Created Successfully")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print("\nFirst 10 Predictions:")
print(predictions[:10])