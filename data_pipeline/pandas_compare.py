import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect("data_pipeline/books.db")


# --------------------------------------------------
# PART 1: Read SQL query results using pd.read_sql
# --------------------------------------------------

sql_join_query = """
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

sql_result = pd.read_sql(sql_join_query, connection)

print("SQL JOIN result using pd.read_sql():")
print(sql_result)


# --------------------------------------------------
# PART 2: Read tables into pandas
# --------------------------------------------------

books_df = pd.read_sql(
    "SELECT * FROM books",
    connection
)

categories_df = pd.read_sql(
    "SELECT * FROM categories",
    connection
)


# --------------------------------------------------
# PART 3: Reproduce the JOIN using pd.merge()
# --------------------------------------------------

merged_result = pd.merge(
    books_df,
    categories_df,
    on="category_id",
    how="inner"
)


# Select the same columns as the SQL query
merged_result = merged_result[
    ["title", "category_name", "rating", "price_gbp"]
]

# Apply the same WHERE condition
merged_result = merged_result[
    merged_result["rating"] >= 4
]

# Apply the same ORDER BY
merged_result = merged_result.sort_values(
    by=["rating", "price_gbp"],
    ascending=[False, False]
)

# Apply the same LIMIT 10
merged_result = merged_result.head(10)


print("\nJOIN result using pd.merge():")
print(merged_result)


# --------------------------------------------------
# PART 4: Compare both results
# --------------------------------------------------

sql_check = sql_result.reset_index(drop=True)
merge_check = merged_result.reset_index(drop=True)

same_result = sql_check.equals(merge_check)

print("\nDo both approaches produce the same result?")
print(same_result)


# Save comparison results
sql_result.to_csv(
    "data_pipeline/read_sql_result.csv",
    index=False
)

merged_result.to_csv(
    "data_pipeline/merge_result.csv",
    index=False
)

print("\nComparison results saved successfully.")


# Close connection
connection.close()