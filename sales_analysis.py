import pandas as pd

# Step 1: Read the dataset
df = pd.read_csv("retail_sales.csv")

print("Original Sales Data:")
print(df)

# Check missing values
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna(subset=["Date", "Product", "Region", "Quantity", "Price"])

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]
print(df.head())

# Display total revenue
total_revenue = df["Revenue"].sum()
print("Total Revenue:", total_revenue)

# Sales by product
product_sales = df.groupby("Product")["Quantity"].sum()
print(product_sales.sort_values(ascending=False))

# Sales by region
region_sales = df.groupby("Region")["Revenue"].sum()
print(region_sales.sort_values(ascending=False))

# Monthly sales
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("\nMonthly Revenue:")
print(df.groupby("Month")["Revenue"].sum())

# Save cleaned data
df.to_csv("cleaned_retail_sales.csv", index=False)

print("\nAnalysis completed successfully!")