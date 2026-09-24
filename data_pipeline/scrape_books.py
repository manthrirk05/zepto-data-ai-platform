import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_rating(article):
    rating_tag = article.select_one("p.star-rating")

    if rating_tag:
        classes = rating_tag.get("class", [])
        for value in ["One", "Two", "Three", "Four", "Five"]:
            if value in classes:
                return int({
                    "One": 1,
                    "Two": 2,
                    "Three": 3,
                    "Four": 4,
                    "Five": 5
                }[value])

    return None


def get_category(book_url):
    response = requests.get(book_url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    breadcrumb = soup.select("ul.breadcrumb li a")

    if len(breadcrumb) >= 3:
        return breadcrumb[2].get_text(strip=True)

    return "Unknown"


def scrape_books():
    books = []

    # First 5 pages = up to 100 books
    for page_number in range(1, 6):

        if page_number == 1:
            url = BASE_URL
        else:
            url = urljoin(
                BASE_URL,
                f"catalogue/page-{page_number}.html"
            )

        print(f"Scraping page {page_number}...")

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )
        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        articles = soup.select(
            "article.product_pod"
        )

        for article in articles:

            title = article.h3.a["title"]

            price = article.select_one(
                ".price_color"
            ).get_text(strip=True)

            availability = article.select_one(
                ".availability"
            ).get_text(" ", strip=True)

            rating = get_rating(article)

            book_link = article.h3.a["href"]

            book_url = urljoin(
                url,
                book_link
            )

            category = get_category(book_url)

            books.append(
                {
                    "title": title,
                    "price": price,
                    "star_rating": rating,
                    "availability": availability,
                    "category": category
                }
            )

    return pd.DataFrame(books)


if __name__ == "__main__":

    df = scrape_books()

    print("\nTotal books scraped:", len(df))

    print("\nCategories found:")
    print(df["category"].value_counts())

    print("\nFirst 5 books:")
    print(df.head())

    df.to_csv(
        "books_raw.csv",
        index=False
    )

    print("\nSaved as books_raw.csv")