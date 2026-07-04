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


pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)
# Check columns and data types for interactions
print("=== Interactions Info ===")
interactions.info()

# Preview the first 5 rows
print("\n=== Interactions Preview ===")
print(interactions.head())

# Set up a grid with 2 plots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Plot 1: Breakdown of Interaction Types
sns.countplot(data=interactions, y='interaction_type', ax=axes[0], palette='Set1',
              order=interactions['interaction_type'].value_counts().index)
axes[0].set_title('Frequency of Interaction Types')
axes[0].set_ylabel('Interaction Type')
axes[0].set_xlabel('Count')

# Plot 2: Distribution of Dwell Time (Converting ms to seconds for easier reading)
interactions['dwell_time_seconds'] = interactions['dwell_time_ms'] / 1000

sns.histplot(data=interactions, x='dwell_time_seconds', bins=30, kde=True, ax=axes[1], color='purple')
axes[1].set_title('Distribution of Dwell Time (in Seconds)')
axes[1].set_xlabel('Dwell Time (Seconds)')
axes[1].set_ylabel('Count')

plt.tight_layout()
plt.show()