# Step 1: Import Required Libraries
import pandas as pd
import numpy as np

# Step 2: Load the Dataset
# Make sure the file is in your working directory or provide the full path
df = pd.read_excel("Online_Retail.xlsx", engine="openpyxl")  # You can also use 'xlrd' for .xls

# Step 3: Preview the Dataset
print("Initial Shape:", df.shape)
print(df.head())

# Step 4: Basic Info
print("\nDataset Info:")
df.info()

# Step 5: Remove Rows with Missing Customer IDs
df = df.dropna(subset=['CustomerID'])

# Step 6: Remove Cancelled Invoices (those starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Step 7: Remove Duplicates
df = df.drop_duplicates()

# Step 8: Convert InvoiceDate to Datetime Format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Step 9: Remove Rows with Zero or Negative Quantity and Price
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Step 10: Clean Whitespaces in Description and Country
df['Description'] = df['Description'].str.strip()
df['Country'] = df['Country'].str.strip()

# Step 11: Remove Rows with Blank Descriptions or StockCode
df = df[df['Description'].notna() & df['StockCode'].notna()]
df = df[~df['Description'].str.lower().isin(['', 'nan'])]

# Step 12: Remove Invoices with Unrealistic Prices (Optional - threshold-based outlier filter)
# Example: Remove unit prices > 10,000 which may be data errors
df = df[df['UnitPrice'] < 10000]

# Step 13: Remove Invalid StockCodes (Optional - non-numeric codes for promotion etc.)
df = df[df['StockCode'].notna() & df['StockCode'].str.match(r'^[A-Za-z0-9]+$')]


# Step 14: Add Calculated Fields
df['Revenue'] = df['Quantity'] * df['UnitPrice']
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Day'] = df['InvoiceDate'].dt.day
df['Hour'] = df['InvoiceDate'].dt.hour

# Step 15: Final Cleaned Dataset Overview
print("\nCleaned Dataset Info:")
df.info()
print("\nSample Cleaned Data:")
print(df.head())

# Step 16: Save Cleaned Data to CSV (optional)
# df.to_csv("cleaned_online_retail.csv", index=False)
