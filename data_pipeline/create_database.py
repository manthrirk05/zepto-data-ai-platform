import sqlite3
import pandas as pd


CSV_FILE = "books_clean.csv"
DATABASE_FILE = "books.db"


# Load cleaned data
df = pd.read_csv(CSV_FILE)


# Create database connection
connection = sqlite3.connect(DATABASE_FILE)


# Create categories table
connection.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT UNIQUE
)
""")


# Insert unique categories
categories = sorted(df["category"].dropna().unique())

for category_id, category_name in enumerate(categories, start=1):
    connection.execute(
        """
        INSERT OR IGNORE INTO categories
        (category_id, category_name)
        VALUES (?, ?)
        """,
        (category_id, category_name)
    )


# Create books table
connection.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price_gbp REAL,
    price_inr REAL,
    rating INTEGER,
    in_stock INTEGER,
    category_id INTEGER,
    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
)
""")


# Clear old book records if script is run again
connection.execute("DELETE FROM books")


# Insert books
for _, row in df.iterrows():

    category_id = connection.execute(
        """
        SELECT category_id
        FROM categories
        WHERE category_name = ?
        """,
        (row["category"],)
    ).fetchone()[0]

    connection.execute(
        """
        INSERT INTO books
        (
            title,
            price_gbp,
            price_inr,
            rating,
            in_stock,
            category_id
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            row["title"],
            row["price_gbp"],
            row["price_inr"],
            row["rating"],
            int(row["in_stock"]),
            category_id
        )
    )


connection.commit()


# Check database
book_count = connection.execute(
    "SELECT COUNT(*) FROM books"
).fetchone()[0]

category_count = connection.execute(
    "SELECT COUNT(*) FROM categories"
).fetchone()[0]


print("\nDatabase created successfully!")

print("Books:", book_count)
print("Categories:", category_count)

print("\nTables:")
print(
    connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()
)


connection.close()