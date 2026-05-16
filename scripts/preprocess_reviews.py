import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Initial Dataset Shape:")
print(df.shape)

# Remove duplicate reviews
before_duplicates = len(df)

df = df.drop_duplicates(subset=["review"])

after_duplicates = len(df)

duplicates_removed = before_duplicates - after_duplicates

print(f"\nDuplicates Removed: {duplicates_removed}")

# Handle missing values
missing_before = df.isnull().sum()

print("\nMissing Values Before Cleaning:")
print(missing_before)

# Drop rows missing review or rating
df = df.dropna(subset=["review", "rating"])

missing_after = df.isnull().sum()

print("\nMissing Values After Cleaning:")
print(missing_after)

# Normalize dates
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Keep only required columns
df = df[["review", "rating", "date", "bank", "source"]]


# Final Dataset Info
print("\nFinal Dataset Shape:")
print(df.shape)

print("\nSample Cleaned Data:")
print(df.head())

# Save cleaned dataset
output_path = "data/raw/bank_reviews_cleaned.csv"

df.to_csv(output_path, index=False)

print(f"\nCleaned dataset saved to: {output_path}")