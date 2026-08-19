import pandas as pd
from itertools import combinations
from collections import Counter
df = pd.read_csv("train.csv")
df["date"] = pd.to_datetime(df["date"])
df = df[df["sales"] > 0]
transactions = df.groupby(
    ["date", "store_nbr"]
)["family"].apply(list)
pair_counts = Counter()
for products in transactions:
    unique_products = sorted(set(products))

    for product_pair in combinations(unique_products, 2):
        pair_counts[product_pair] += 1
top_pairs = pair_counts.most_common(10)
print("Week 2 Day 6: Product Recommendations")
print("--------------------------------------")
print("Top 10 Frequently Bought Together Product Categories:\n")
for pair, count in top_pairs:
    print(f"{pair[0]} + {pair[1]}: {count} transactions")