import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV (or Excel)
df = pd.read_csv("cleaned_online_retail.csv")

# Clean & prepare dataframes

# Customers: unique CustomerID and Country, drop missing CustomerID
df_customers = df[['CustomerID', 'Country']].drop_duplicates()
df_customers = df_customers[df_customers['CustomerID'].notna()]

# Products: unique StockCode and Description, drop duplicates on StockCode
df_products = df[['StockCode', 'Description']].drop_duplicates(subset=['StockCode'])
df_products['StockCode'] = df_products['StockCode'].astype(str)

# Invoices: unique InvoiceNo, InvoiceDate, CustomerID
df_invoices = df[['InvoiceNo', 'InvoiceDate', 'CustomerID']].drop_duplicates()
df_invoices['InvoiceDate'] = pd.to_datetime(df_invoices['InvoiceDate'])
df_invoices['InvoiceNo'] = df_invoices['InvoiceNo'].astype(str)
df_invoices['CustomerID'] = df_invoices['CustomerID'].astype(int)

# InvoiceItems: InvoiceNo, StockCode, Quantity, UnitPrice
df_invoice_items = df[['InvoiceNo', 'StockCode', 'Quantity', 'UnitPrice']].copy()
df_invoice_items['InvoiceNo'] = df_invoice_items['InvoiceNo'].astype(str)
df_invoice_items['StockCode'] = df_invoice_items['StockCode'].astype(str)

# Database connection string
connection_string = (
    "mssql+pyodbc://@ANURAG\\MSSQLSERVER01/ProjectDB"
    "?driver=ODBC+Driver+18+for+SQL Server&Trusted_Connection=yes&TrustServerCertificate=yes"
)
engine = create_engine(connection_string, fast_executemany=True)

# Insert function to handle exceptions
def insert_table(df, table_name):
    try:
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        print(f"✅ Inserted data into {table_name} successfully!")
    except Exception as e:
        print(f"❌ Error inserting into {table_name}: {e}")

# Run insertions in order respecting foreign keys
# Make sure you truncated tables beforehand in SSMS or via SQL commands before this script runs
insert_table(df_customers, 'Customers')
insert_table(df_products, 'Products')
insert_table(df_invoices, 'Invoices')
insert_table(df_invoice_items, 'InvoiceItems')

# Dispose engine after use
engine.dispose()
