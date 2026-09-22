import pandas as pd

# Load raw scraped data
df = pd.read_csv("data_pipeline/raw_books.csv")

print("Raw data:")
print(df.head())

print("\nData types:")
print(df.dtypes)

# Clean price 
df["price_gbp"] = ( 
    df["price"] 
    .astype(str) 
    .str.replace("£", "", regex=False) 
    .str.replace("Â", "", regex=False) 
    .str.strip() 
) 
 
df["price_gbp"] = pd.to_numeric( 
    df["price_gbp"], 
    errors="coerce" 
) 
 
print("\nCleaned price:") 
print(df[["price", "price_gbp"]].head())

# Convert star ratings to integers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["star_rating"].map(rating_map)

print("\nConverted ratings:")
print(df[["star_rating", "rating"]].head())

# Convert availability to Boolean
df["in_stock"] = (
    df["availability"]
    .str.strip()
    .str.lower()
    .eq("in stock")
)

print("\nConverted availability:")
print(df[["availability", "in_stock"]].head())

# Check for missing values after parsing
print("\nMissing values:")
print(df[["price_gbp", "rating", "in_stock"]].isna().sum())

# Handle invalid price values using median imputation
price_median = df["price_gbp"].median()

df["price_gbp"] = df["price_gbp"].fillna(price_median)

# Handle invalid rating values using median imputation
rating_median = df["rating"].median()

df["rating"] = df["rating"].fillna(rating_median).round().astype(int)

print("\nAfter imputation:")
print(df[["price_gbp", "rating"]].isna().sum())

# Convert GBP to INR using the required fixed project rate
GBP_TO_INR = 105.50

df["price_inr"] = df["price_gbp"] * GBP_TO_INR

print("\nPrices after GBP to INR conversion:")
print(df[["price_gbp", "price_inr"]].head())

# Save cleaned data
df.to_csv("data_pipeline/clean_books.csv", index=False)

print("\nCleaned data saved to data_pipeline/clean_books.csv")