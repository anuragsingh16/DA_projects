# Sales and Customer Analytics Dashboard Project

## 📄 Project Title

**Sales and Customer Insights using Python, SQL Server, and Power BI**

---

## 📆 Step 1: Data Cleaning and Preprocessing (Python)

### Dataset Used: https://archive.ics.uci.edu/dataset/352/online+retail

* **Online Retail Dataset** (Excel/CSV format)

### Libraries Used:

```python
import pandas as pd
import numpy as np
```

### Key Cleaning Steps:

1. **Load Data**

```python
df = pd.read_excel('Online_Retail.xlsx')
```

2. **Drop Null Values**

```python
df.dropna(inplace=True)
```

3. **Remove Canceled Orders**

```python
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
```

4. **Filter Positive Quantity and Price**

```python
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
```

5. **Generate Additional Fields**

```python
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.to_period('M')
```

---

## 📆 Step 2: Database Setup in Microsoft SQL Server (SSMS)

### Tables Created:

* **Customers**
* **Invoices**
* **InvoiceItems**
* **Products**

### Schema Design:

```sql
CREATE TABLE Customers (
  CustomerID INT PRIMARY KEY,
  Country NVARCHAR(50)
);

CREATE TABLE Invoices (
  InvoiceNo NVARCHAR(20) PRIMARY KEY,
  InvoiceDate DATETIME,
  CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID)
);

CREATE TABLE Products (
  StockCode NVARCHAR(20) PRIMARY KEY,
  Description NVARCHAR(255)
);

CREATE TABLE InvoiceItems (
  InvoiceItemID INT IDENTITY(1,1) PRIMARY KEY,
  InvoiceNo NVARCHAR(20) FOREIGN KEY REFERENCES Invoices(InvoiceNo),
  StockCode NVARCHAR(20) FOREIGN KEY REFERENCES Products(StockCode),
  Quantity INT,
  UnitPrice FLOAT
);
```

### Data Import:

Use SQL Server Import Wizard or Python `pyodbc`/`sqlalchemy` to push cleaned data into respective tables.

---

## 🔍 Step 3: Connecting SQL Server to Power BI

### Steps:

1. Open Power BI Desktop
2. Click on **"Get Data" > "SQL Server"**
3. Enter:

   * Server: `localhost\\SQLEXPRESS` or your server name
   * Database: `OnlineRetailDB`
   * Use **Import** or **DirectQuery**
4. Select required tables
5. Load data into the model

---

## 📊 Step 4: Building the Dashboard Visualizations

### ✅ 1) Monthly Sales Trend

**Visual Type**: Line Chart

* **Axis**: InvoiceDate (Month)
* **Values**: Total Revenue (Sum of Quantity \* UnitPrice)
* **Insight**: Tracks monthly performance of the business.

### ✅ 2) Top 10 Selling Products

**Visual Type**: Bar Chart (Descending)

* **Axis**: Product Description
* **Values**: Total Quantity Sold
* **Filter**: Top 10
* **Insight**: Displays best-selling products by volume.

### ✅ 3) Revenue and Quantity by Country & Description

**Visual Type**: Clustered Bar or Matrix

* **Axis**: Country, Product Description
* **Values**: Total Revenue and Quantity Sold
* **Insight**: Understand product sales trends across regions.

### ✅ 4) Top 5 Countries by Revenue

**Visual Type**: Donut Chart or Bar Chart

* **Axis**: Country
* **Values**: Total Revenue
* **Filter**: Top 5 by Revenue
* **Insight**: Identifies strongest geographical markets.

---

## 🚀 Outcomes and Impact

* Built a clean and scalable relational data model in SQL Server.
* Created interactive and dynamic dashboards using Power BI.
* Enabled stakeholder visibility into product performance and customer geography.
* Demonstrated end-to-end BI workflow from raw data to visual insights.

---

## 📅 Author

**Anurag**
Engineer | Data Analyst | Entrepreneur

---

## 📖 License

For educational and portfolio use. Dataset source: UCI Machine Learning Repository.
