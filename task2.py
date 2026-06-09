import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\superstore.csv")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Order Date.1'] = pd.to_datetime(df['Order Date.1'], dayfirst=True)

# Save cleaned dataset
df.to_csv(r"C:\Users\LENOVO\OneDrive\Desktop\cleaned_superstore.csv", index=False)

print("\nData Cleaning Completed Successfully!")

