import sqlite3
import pandas as pd

# Load cleaned data
df = pd.read_csv("data_pipeline/clean_books.csv")

# Create SQLite database
connection = sqlite3.connect("data_pipeline/books.db")

cursor = connection.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON")

# Create categories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT UNIQUE NOT NULL
)
""")

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
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

# Get unique categories
categories = sorted(df["category"].dropna().unique())

# Insert categories
for category_id, category_name in enumerate(categories, start=1):
    cursor.execute(
        """
        INSERT OR IGNORE INTO categories
        (category_id, category_name)
        VALUES (?, ?)
        """,
        (category_id, category_name)
    )

# Create category → ID mapping
category_mapping = {
    category_name: category_id
    for category_id, category_name in enumerate(categories, start=1)
}

# Add category_id to the DataFrame
df["category_id"] = df["category"].map(category_mapping)

# Insert books
for book_id, row in enumerate(df.itertuples(index=False), start=1):
    cursor.execute(
        """
        INSERT INTO books
        (
            book_id,
            title,
            price_gbp,
            price_inr,
            rating,
            in_stock,
            category_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            book_id,
            row.title,
            row.price_gbp,
            row.price_inr,
            row.rating,
            int(row.in_stock),
            row.category_id
        )
    )

# Save changes
connection.commit()

print("Data inserted successfully.")

# Check number of rows
cursor.execute("SELECT COUNT(*) FROM categories")
category_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM books")
book_count = cursor.fetchone()[0]

print("Number of categories:", category_count)
print("Number of books:", book_count)

# Close database connection
connection.close()