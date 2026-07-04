import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dynamically get the directory where your current script/notebook is running
current_dir = os.getcwd()

# Load the datasets directly from that folder
users = pd.read_csv(os.path.join(current_dir, 'users.csv'))
sessions = pd.read_csv(os.path.join(current_dir, 'sessions.csv'))
interactions = pd.read_csv(os.path.join(current_dir, 'interactions.csv'))
products = pd.read_csv(os.path.join(current_dir, 'products.csv'))
purchases = pd.read_csv(os.path.join(current_dir, 'purchases.csv'))
reviews = pd.read_csv(os.path.join(current_dir, 'reviews.csv'))

# Define the dictionary for the loop
dfs = {
    "Users": users,
    "Sessions": sessions,
    "Interactions": interactions,
    "Products": products,
    "Purchases": purchases,
    "Reviews": reviews
}


# 1. Set Pandas options to display all columns and wide text without truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

# Check columns and data types for products
print("=== Products Info ===")
products.info()

# Preview the first 5 rows
print("\n=== Products Preview ===")
print(products.head())

# Set up a grid of 2 plots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Top product categories in inventory
sns.countplot(data=products, y='category', ax=axes[0], palette='Set2',
              order=products['category'].value_counts().index)
axes[0].set_title('Product Count by Category')
axes[0].set_xlabel('Number of Products')
axes[0].set_ylabel('Category')

# Plot 2: Price distribution of products
sns.histplot(data=products, x='price', bins=30, kde=True, ax=axes[1], color='darkgreen')
axes[1].set_title('Distribution of Product Prices')
axes[1].set_xlabel('Price ($)')
axes[1].set_ylabel('Count')

plt.tight_layout()


# Set up a grid with 3 subplots side-by-side
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Option 1 Rating Distribution: Using .dropna() so Seaborn completely ignores the missing 548 values
sns.histplot(data=products['rating_avg'].dropna(), bins=10, kde=True, ax=axes[0], color='gold')
axes[0].set_title('Distribution of Product Ratings\n(Rated Items Only)')
axes[0].set_xlabel('Average Rating (1-5 Stars)')
axes[0].set_ylabel('Count of Products')

# 2. Stock Quantity Distribution
sns.histplot(data=products, x='stock_quantity', bins=20, kde=True, ax=axes[1], color='teal')
axes[1].set_title('Distribution of Stock Quantities')
axes[1].set_xlabel('Items in Stock')
axes[1].set_ylabel('Count')

# 3. Top Brands (Taking top 10 brands so it fits neatly)
top_brands = products['brand'].value_counts().head(10)
sns.barplot(x=top_brands.values, y=top_brands.index, ax=axes[2], palette='cubehelix')
axes[2].set_title('Top 10 Brands by Product Count')
axes[2].set_xlabel('Number of Products')
axes[2].set_ylabel('Brand')

plt.tight_layout()
plt.show()