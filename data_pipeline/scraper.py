import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

base_url = "https://books.toscrape.com/"

all_books = []

# Scrape first 5 pages
for page_number in range(1, 6):

    if page_number == 1:
        page_url = base_url
    else:
        page_url = urljoin(
            base_url,
            f"catalogue/page-{page_number}.html"
        )

    print(f"Scraping page {page_number}: {page_url}")

    response = requests.get(page_url)

    if response.status_code != 200:
        print(f"Could not access page {page_number}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    for book in books:

        # Title
        title = book.h3.a["title"]

        # Price
        price = book.select_one(".price_color").text.strip()

        # Star rating
        star_rating = book.select_one(".star-rating")["class"][1]

        # Availability
        availability = book.select_one(".availability").text.strip()

        # Book detail page
        book_link = book.h3.a["href"]
        book_url = urljoin(page_url, book_link)

        # Open book detail page
        book_response = requests.get(book_url)

        if book_response.status_code != 200:
            category = "Unknown"
        else:
            book_soup = BeautifulSoup(
                book_response.text,
                "html.parser"
            )

            breadcrumb = book_soup.select("ul.breadcrumb li")

            if len(breadcrumb) >= 3:
                category = breadcrumb[2].get_text(strip=True)
            else:
                category = "Unknown"

        all_books.append({
            "title": title,
            "price": price,
            "star_rating": star_rating,
            "availability": availability,
            "category": category
        })

print("\nTotal books scraped:", len(all_books))

# Convert to pandas DataFrame
df = pd.DataFrame(all_books)

print("\nFirst 5 rows:")
print(df.head())

print("\nCategories:")
print(df["category"].value_counts())

# Save raw scraped data
df.to_csv("data_pipeline/raw_books.csv", index=False)
print("\nRaw data saved to data_pipeline/raw_books.csv")