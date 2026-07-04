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

# Check purchases structure
print("=== Purchases Info ===")
purchases.info()

# Check reviews structure
print("\n=== Reviews Info ===")
reviews.info()

# Preview them
print("\n=== Previews ===")
print("Purchases Head:")
print(purchases.head(2))
print("\nReviews Head:")
print(reviews.head(2))

# Set up a grid of 2 plots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(16, 5))

# Plot 1: Total Amount spent per purchase transaction
sns.histplot(data=purchases, x='total_amount', bins=30, kde=True, ax=axes[0], color='darkblue')
axes[0].set_title('Distribution of Purchase Total Amounts')
axes[0].set_xlabel('Total Amount ($)')
axes[0].set_ylabel('Count')

# Plot 2: Distribution of Individual Review Ratings
# We use countplot here because individual review scores are whole integer stars (1, 2, 3, 4, 5)
sns.countplot(data=reviews, x='rating', ax=axes[1], palette='Reds')
axes[1].set_title('Distribution of Scores in Customer Reviews')
axes[1].set_xlabel('Review Rating (Stars)')
axes[1].set_ylabel('Count')

plt.tight_layout()
plt.show()