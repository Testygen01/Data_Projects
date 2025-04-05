import pandas as pd 

# Load csv
df = pd.read_csv("airtravel.csv")

# Explore the data
print(df.head())
print(df.info())

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Check for nulls or strange values
print("\nMissing Values:\n", df.isnull().sum())

# save cleaned data
df.to_csv("Cleaned_airtravel.csv", index=False)
print("\n Cleaned CSV saved.")