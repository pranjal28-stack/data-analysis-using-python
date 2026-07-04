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
# 1. Merge the Users and Purchases dataframes on 'user_id'
# We use an inner join so we only keep users who have actually made a purchase
user_purchases = pd.merge(purchases, users, on='user_id', how='inner')

# Set up a grid of 2 plots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Income Level vs Total Purchase Amount (Boxplot)
income_order = ['low', 'medium', 'high', 'very_high']
sns.boxplot(data=user_purchases, x='income_level', y='total_amount', 
            ax=axes[0], palette='magma', order=income_order)
axes[0].set_title('Purchase Amounts by User Income Level', fontsize=13)
axes[0].set_xlabel('Income Level')
axes[0].set_ylabel('Total Purchase Amount ($)')

# Plot 2: Loyalty Tier vs Total Purchase Amount (Boxplot)
loyalty_order = ['bronze', 'silver', 'gold', 'platinum']
sns.boxplot(data=user_purchases, x='loyalty_tier', y='total_amount', 
            ax=axes[1], palette='viridis', order=loyalty_order)
axes[1].set_title('Purchase Amounts by Loyalty Tier', fontsize=13)
axes[1].set_xlabel('Loyalty Tier')
axes[1].set_ylabel('Total Purchase Amount ($)')

plt.tight_layout()
plt.show()