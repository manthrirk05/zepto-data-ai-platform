import pandas as pd


INPUT_FILE = "books_raw.csv"
OUTPUT_FILE = "books_clean.csv"

GBP_TO_INR = 105.50


df = pd.read_csv(INPUT_FILE)


df["price_gbp"] = (
    df["price"]
    .str.extract(r"(\d+(?:\.\d+)?)")[0]
    .astype(float)
)


# Convert GBP to INR
df["price_inr"] = df["price_gbp"] * GBP_TO_INR


# Clean availability
df["in_stock"] = df["availability"].str.contains(
    "In stock",
    case=False,
    na=False
)


# Clean rating
df["rating"] = df["star_rating"].astype(int)


# Keep required columns
df = df[
    [
        "title",
        "price_gbp",
        "price_inr",
        "rating",
        "in_stock",
        "category"
    ]
]


# Save cleaned data
df.to_csv(
    OUTPUT_FILE,
    index=False
)


print("\nCleaning completed successfully!")

print("\nData shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSaved as:", OUTPUT_FILE)