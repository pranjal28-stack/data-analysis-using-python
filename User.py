import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
# Check columns and data types
print("=== Users Info ===")
print(users.info())

# Preview the first 5 rows
print("\n=== Users Preview ===")
print(users.head())


# Create a figure with two subplots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Distribution of User Age (Histogram)
sns.histplot(data=users, x='age', bins=20, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution of User Age')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Count')

# Plot 2: Breakdown of Loyalty Tiers (Countplot)
# (Assuming order if bronze, silver, gold exist)
sns.countplot(data=users, x='loyalty_tier', ax=axes[1], palette='viridis', 
              order=users['loyalty_tier'].value_counts().index)
axes[1].set_title('Number of Users by Loyalty Tier')
axes[1].set_xlabel('Loyalty Tier')
axes[1].set_ylabel('Count')

plt.tight_layout()
plt.show()

# Set up a grid of 3 plots (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Gender Breakdown
sns.countplot(data=users, x='gender', ax=axes[0], palette='pastel')
axes[0].set_title('Gender Distribution')
axes[0].set_xlabel('Gender')
axes[0].set_ylabel('Count')

# Plot 2: Income Level Breakdown
income_order = ['low', 'medium', 'high', 'very_high'] # logical ordering
sns.countplot(data=users, x='income_level', ax=axes[1], palette='magma', order=income_order)
axes[1].set_title('Income Level Distribution')
axes[1].set_xlabel('Income Level')
axes[1].set_ylabel('Count')

# Plot 3: Top Preferred Categories (Horizontal for readability)
sns.countplot(data=users, y='preferred_category', ax=axes[2], palette='Set2',
              order=users['preferred_category'].value_counts().index)
axes[2].set_title('Preferred Categories')
axes[2].set_xlabel('Count')
axes[2].set_ylabel('Category')

plt.tight_layout()
plt.show()


# 1. Convert signup_date column to datetime format
users['signup_date'] = pd.to_datetime(users['signup_date'])

# 2. Extract Year-Month for grouping
users['signup_month'] = users['signup_date'].dt.to_period('M')

# 3. Count signups per month and sort chronologically
monthly_signups = users.groupby('signup_month').size()
monthly_signups.index = monthly_signups.index.to_timestamp() # Convert back to timestamp for plotting

# 4. Plot the trend over time
plt.figure(figsize=(12, 5))
sns.lineplot(x=monthly_signups.index, y=monthly_signups.values, marker='o', color='b', linewidth=2)

plt.title('User Signup Trend Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of New Signups', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()