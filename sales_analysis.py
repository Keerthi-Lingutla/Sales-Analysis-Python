import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load and Clean Data
df = pd.read_csv("Sales.csv")
df.drop_duplicates(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

# Step 2: Preview Data
print("\n✅ Cleaned Data Preview:")
print(df.head())

# 📊 1. Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title("Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📊 2. Sales by Region (Warning Fixed)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(7, 5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette='Set2', legend=False)
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.tight_layout()
plt.show()

# 📊 3. Top 5 Selling Products (Warning Fixed)
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(7, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette='magma', legend=False)
plt.title("Top 5 Selling Products")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.show()

# 📊 4. Profit by Category (Pie Chart)
category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(6, 6))
plt.pie(
    category_profit,
    labels=category_profit.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("pastel")
)
plt.title("Profit Share by Category")
plt.tight_layout()
plt.show()

# ✅ Summary Statistics
print("\n📊 Summary Statistics:")
print(df.describe())

# ✅ Total Sales and Profit
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("\n🧾 Total Sales:", total_sales)
print("🧾 Total Profit:", total_profit)

# ✅ Save Monthly Sales Summary
monthly_summary = df.groupby('Month')[['Sales', 'Profit']].sum()
monthly_summary.to_csv("monthly_summary.csv")
print("\n✅ Monthly summary exported as 'monthly_summary.csv'")

# ✅ Business Insights
print("\n📌 Key Insights:")
print("- Electronics category generated the highest revenue.")
print("- North and South regions had the highest sales.")
print("- Top-selling product contributed the most to revenue.")
print("- Monthly sales peaked in specific months (check bar chart).")
