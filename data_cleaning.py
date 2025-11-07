# data_cleaning.py
import pandas as pd

# Step 1: Load dataset
file_path ="c:\Users\Ramanan\Downloads\Kaggle datasets\BMW sales data (2010-2024) (1).csv"
df = pd.read_csv(file_path)

# Step 2: Inspect the dataset
print(" Data Overview:")
print(df.info())
print("\nFirst 5 rows:\n", df.head())

# Step 3: Handle missing values
print("\nMissing Values Before Cleaning:\n", df.isnull().sum())
df = df.drop_duplicates()
df = df.fillna({
    "Color": "Unknown",
    "Fuel_Type": "Unknown",
    "Transmission": "Unknown"
})
print("\nMissing Values After Cleaning:\n", df.isnull().sum())

# Step 4: Remove outliers (example: using Mileage_KM)
Q1 = df["Mileage_KM"].quantile(0.25)
Q3 = df["Mileage_KM"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["Mileage_KM"] >= (Q1 - 1.5 * IQR)) & (df["Mileage_KM"] <= (Q3 + 1.5 * IQR))]

# Step 5: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 6: Convert data types (if needed)
df['year'] = df['year'].astype(int)
df['price_usd'] = df['price_usd'].astype(float)

# Step 7: Save the cleaned dataset
cleaned_path = "cleaned_bmw_sales.csv"
df.to_csv(cleaned_path, index=False)
print(f"\nCleaned data saved to: {cleaned_path}")

# Step 8: Summary stats
print("\n Summary Statistics:")
print(df.describe())
