import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("data_pipeline/books.db")

# File to save SQL queries and outputs
output_file = open("data_pipeline/sql_results.md", "w", encoding="utf-8")


def run_query(query_number, title, query):
    print(f"\n{title}")
    print("-" * len(title))

    cursor = connection.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Save query and output
    output_file.write(f"## {title}\n\n")
    output_file.write("### SQL Query\n\n")
    output_file.write("```sql\n")
    output_file.write(query.strip())
    output_file.write("\n```\n\n")

    output_file.write("### Output\n\n")
    output_file.write("```text\n")

    for row in rows:
        output_file.write(str(row) + "\n")

    output_file.write("```\n\n")


# Query 1: SELECT + WHERE
query1 = """
SELECT title, rating, price_gbp
FROM books
WHERE rating >= 4;
"""

run_query(
    1,
    "QUERY 1 — Books with rating 4 or higher",
    query1
)


# Query 2: ORDER BY + LIMIT
query2 = """
SELECT title, price_gbp
FROM books
ORDER BY price_gbp DESC
LIMIT 10;
"""

run_query(
    2,
    "QUERY 2 — 10 Most Expensive Books",
    query2
)


# Query 3: DISTINCT + IN + JOIN
query3 = """
SELECT DISTINCT c.category_name
FROM books b
JOIN categories c
    ON b.category_id = c.category_id
WHERE c.category_name IN ('Poetry', 'Fiction', 'Mystery');
"""

run_query(
    3,
    "QUERY 3 — Selected Categories",
    query3
)


# Query 4: BETWEEN
query4 = """
SELECT title, price_gbp, rating
FROM books
WHERE price_gbp BETWEEN 20 AND 40
ORDER BY price_gbp;
"""

run_query(
    4,
    "QUERY 4 — Books priced between £20 and £40",
    query4
)


# Query 5: JOIN
query5 = """
SELECT
    b.title,
    c.category_name,
    b.rating,
    b.price_gbp
FROM books b
JOIN categories c
    ON b.category_id = c.category_id
WHERE b.rating >= 4
ORDER BY b.rating DESC, b.price_gbp DESC
LIMIT 10;
"""

run_query(
    5,
    "QUERY 5 — Top 10 Highly Rated Books with Categories",
    query5
)


# Close file and database
output_file.close()
connection.close()

print("\nSQL queries and outputs saved to data_pipeline/sql_results.md")