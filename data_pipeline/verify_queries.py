import sqlite3
import pandas as pd


DATABASE_FILE = "books.db"


connection = sqlite3.connect(DATABASE_FILE)


queries = {
    "Query 1 - Total books": """
        SELECT COUNT(*) AS total_books
        FROM books;
    """,

    "Query 2 - Average price": """
        SELECT ROUND(AVG(price_inr), 2) AS average_price_inr
        FROM books;
    """,

    "Query 3 - Books by rating": """
        SELECT
            rating,
            COUNT(*) AS book_count
        FROM books
        GROUP BY rating
        ORDER BY rating;
    """,

    "Query 4 - Most expensive books": """
        SELECT
            title,
            price_inr,
            rating
        FROM books
        ORDER BY price_inr DESC
        LIMIT 10;
    """,

    "Query 5 - Books by category": """
        SELECT
            c.category_name,
            COUNT(b.book_id) AS book_count
        FROM categories c
        JOIN books b
            ON c.category_id = b.category_id
        GROUP BY c.category_name
        ORDER BY book_count DESC;
    """
}


for name, query in queries.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    result = pd.read_sql_query(
        query,
        connection
    )

    print(result.to_string(index=False))


connection.close()

print("\nAll SQL queries executed successfully!")