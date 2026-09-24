# Module 1 — Data Pipeline

## Project Overview

This module builds a complete data pipeline for book catalog data.

The pipeline performs:

1. Web scraping
2. Data cleaning
3. GBP to INR currency conversion
4. SQLite database creation
5. SQL analysis
6. Pandas verification

## Data Source

The data is collected from:

https://books.toscrape.com/

The scraper collects book title, price, rating, availability, and category.

## Pipeline

Website
→ Scraping
→ Raw CSV
→ Data Cleaning
→ Clean CSV
→ SQLite Database
→ SQL Queries
→ Pandas Verification

## Dataset

The final dataset contains:

- 100 books
- 29 categories
- Book title
- Price in GBP
- Price in INR
- Rating
- Stock availability
- Category

## Currency Conversion

The project uses the required fixed conversion rate:

**1 GBP = 105.50 INR**

No external currency API is required.

## Database Schema

### categories

- category_id — Primary Key
- category_name — Unique category name

### books

- book_id — Primary Key
- title
- price_gbp
- price_inr
- rating
- in_stock
- category_id — Foreign Key

## SQL Analysis

The project includes SQL queries for:

- Total number of books
- Average book price
- Books grouped by rating
- Most expensive books
- Books grouped by category
- Average price by category
- Five-star books

## Files

- `scrape_books.py` — Scrapes book data
- `clean_books.py` — Cleans and transforms data
- `create_database.py` — Creates SQLite database
- `queries.sql` — SQL analysis queries
- `verify_queries.py` — Executes SQL queries using Pandas
- `books_raw.csv` — Raw scraped data
- `books_clean.csv` — Cleaned data
- `books.db` — SQLite database

## How to Run

Activate the virtual environment and run:

```bash
python scrape_books.py
python clean_books.py
python create_database.py
python verify_queries.py