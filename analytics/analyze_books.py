import pandas as pd

# Load cleaned data
df = pd.read_csv("data_pipeline/books_clean.csv")

print("Total books:", len(df))
print("Average price (INR):", round(df["price_inr"].mean(), 2))
print("Average rating:", round(df["rating"].mean(), 2))

print("\nBooks by category:")
print(df["category"].value_counts())

print("\nTop 10 expensive books:")
print(
    df[["title", "price_inr"]]
    .sort_values("price_inr", ascending=False)
    .head(10)
)