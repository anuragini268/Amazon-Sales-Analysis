import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# =====================
# Q1 - Load Dataset
# =====================
df = pd.read_csv("Amazon.csv")
print("Dataset Loaded Successfully!")
print(df.head())

# =====================
# Q2 - Dataset Overview
# =====================
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nDescription:\n", df.describe())

# =====================
# Q3 - KPI Analysis
# =====================
print("\n--- KPI Analysis ---")
print("Total Revenue:", df['TotalAmount'].sum())
print("Total Orders:", df['OrderID'].nunique())
print("Average Order Value:", df['TotalAmount'].mean())
print("Total Quantity:", df['Quantity'].sum())
print("Max Order Value:", df['TotalAmount'].max())
print("Min Order Value:", df['TotalAmount'].min())

# =====================
# Q4 - Sales by State
# =====================
print("\n--- Sales by State ---")
state_sales = df.groupby('State')['TotalAmount'].sum().sort_values(ascending=False)
print(state_sales)

# =====================
# Q5 - Sales by Category
# =====================
print("\n--- Sales by Category ---")
print(df.groupby('Category')['TotalAmount'].sum().sort_values(ascending=False))

# =====================
# Q6 - Sales by Brand
# =====================
print("\n--- Sales by Brand ---")
print(df.groupby('Brand')['TotalAmount'].sum().sort_values(ascending=False))

# =====================
# Q7 - Top 5 Customers
# =====================
print("\n--- Top 5 Customers ---")
print(df.groupby('CustomerName')['TotalAmount'].sum().sort_values(ascending=False).head(5))

# =====================
# Q8 - Payment Method
# =====================
print("\n--- Payment Method Count ---")
print(df['PaymentMethod'].value_counts())

# =====================
# Q9 - Monthly Sales
# =====================
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Month'] = df['OrderDate'].dt.to_period('M')
monthly = df.groupby('Month')['TotalAmount'].sum()
print("\n--- Monthly Sales ---")
print(monthly)

# =====================
# Q10 - Charts
# =====================

# Chart 1 - Bar Chart: Sales by State
state_sales.plot(kind='bar', figsize=(12,5), title='Sales by State', color='steelblue')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('sales_by_state.png')
plt.show()
# Sales by State
df.groupby("State")["TotalAmount"].sum().plot(kind="bar")
plt.title("Sales by State")
plt.xlabel("State")
plt.ylabel("Total Sales Amount")
plt.savefig("sales_by_state.png")
plt.close()

# Sales by Category
df.groupby("Category")["TotalAmount"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales Amount")
plt.savefig("sales_by_category.png")
plt.close()

# Payment Method Distribution
df["PaymentMethod"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.savefig("payment_method.png")
plt.close()

# Monthly Sales Trend
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df.groupby(df["OrderDate"].dt.to_period("M"))["TotalAmount"].sum().plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales Amount")
plt.savefig("monthly_trend.png")
plt.close()

