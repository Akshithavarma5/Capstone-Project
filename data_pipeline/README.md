# Module 1 — Data Pipeline

## Project Overview

This module implements an end-to-end data pipeline for collecting book catalogue data from Books to Scrape.

The pipeline performs the following steps:

1. Scrapes book data from the public Books to Scrape website.
2. Collects data from five catalogue pages, resulting in 100 books across multiple categories.
3. Cleans and converts the scraped fields into appropriate data types.
4. Converts book prices from GBP to INR using the fixed project rate.
5. Stores the cleaned data in a normalized SQLite database.
6. Executes SQL queries demonstrating required SQL clauses.
7. Reads SQL results into pandas using `pd.read_sql()`.
8. Reproduces the SQL JOIN using `pd.merge()` and verifies that both approaches produce equivalent results.

---

## Dataset

### Source

Books to Scrape:

https://books.toscrape.com/

The website is a public scraping-practice website and does not require authentication or an API key.

### Scraped Fields

The following fields are collected for every book:

- `title`
- `price`
- `star_rating`
- `availability`
- `category`

The scraper processes the first five catalogue pages and collects 100 books.

---

## Installation

Python 3.13 was used for this project.

Install the required libraries using:

```bash
python -m pip install -r data_pipeline/requirements.txt