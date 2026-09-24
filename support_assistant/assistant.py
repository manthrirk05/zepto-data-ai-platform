import pandas as pd

df = pd.read_csv("data_pipeline/books_clean.csv")


def search_books(keyword):
    results = df[
        df["title"].str.contains(keyword, case=False, na=False)
    ]

    if results.empty:
        print("No books found.")
    else:
        print("\nMatching books:")
        print(results[["title", "price_inr", "rating", "in_stock"]].to_string(index=False))


print("📚 Book Support Assistant")
print("Type a book name to search.")
print("Type 'exit' to stop.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Assistant: Goodbye! 👋")
        break

    search_books(user_input)