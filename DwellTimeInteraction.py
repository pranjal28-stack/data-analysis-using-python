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


# 1. Explicitly create the missing column first
interactions['dwell_time_seconds'] = interactions['dwell_time_ms'] / 1000

plt.figure(figsize=(12, 6))

# 2. Sort the categories by their median dwell time
dwell_order = interactions.groupby('interaction_type')['dwell_time_seconds'].median().sort_values(ascending=False).index

# 3. Create the horizontal boxplot
sns.boxplot(data=interactions, y='interaction_type', x='dwell_time_seconds', 
            palette='Set3', order=dwell_order)

plt.title('Page Dwell Time (Seconds) by Interaction Type', fontsize=14)
plt.xlabel('Dwell Time (Seconds)', fontsize=12)
plt.ylabel('Interaction Type', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()