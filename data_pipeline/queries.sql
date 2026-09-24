-- Query 1: Total number of books
SELECT COUNT(*) AS total_books
FROM books;


-- Query 2: Average price in INR
SELECT ROUND(AVG(price_inr), 2) AS average_price_inr
FROM books;


-- Query 3: Books grouped by rating
SELECT
    rating,
    COUNT(*) AS book_count
FROM books
GROUP BY rating
ORDER BY rating;


-- Query 4: Most expensive books
SELECT
    title,
    price_inr,
    rating
FROM books
ORDER BY price_inr DESC
LIMIT 10;


-- Query 5: Number of books in each category
SELECT
    c.category_name,
    COUNT(b.book_id) AS book_count
FROM categories c
JOIN books b
    ON c.category_id = b.category_id
GROUP BY c.category_name
ORDER BY book_count DESC;


-- Query 6: Average price by category
SELECT
    c.category_name,
    ROUND(AVG(b.price_inr), 2) AS average_price_inr
FROM categories c
JOIN books b
    ON c.category_id = b.category_id
GROUP BY c.category_name
ORDER BY average_price_inr DESC;


-- Query 7: Books with rating 5
SELECT
    b.title,
    b.price_inr,
    c.category_name AS category
FROM books b
JOIN categories c
    ON b.category_id = c.category_id
WHERE b.rating = 5
ORDER BY b.price_inr DESC;