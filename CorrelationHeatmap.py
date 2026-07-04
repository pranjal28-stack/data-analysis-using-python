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

# 1. Calculate total purchase spending per user
user_spend = purchases.groupby('user_id')['total_amount'].sum().reset_index(name='total_user_spend')

# 2. Calculate average dwell time per user
user_dwell = interactions.groupby('user_id')['dwell_time_ms'].mean().reset_index(name='avg_dwell_time_ms')

# 3. Combine with core user profiles table (using 'income_level')
master_numeric = users[['user_id', 'age', 'income_level']].copy()
master_numeric = master_numeric.merge(user_spend, on='user_id', how='left')
master_numeric = master_numeric.merge(user_dwell, on='user_id', how='left')

# Fill users who didn't buy anything with 0 spend
master_numeric['total_user_spend'] = master_numeric['total_user_spend'].fillna(0)

# 4. Map the categorical income levels to numbers so the correlation math works
income_mapping = {'low': 0, 'medium': 1, 'high': 2, 'very_high': 3}
master_numeric['income_numeric'] = master_numeric['income_level'].map(income_mapping)

# 5. Drop the text columns and compute the correlation matrix
corr_features = ['age', 'income_numeric', 'total_user_spend', 'avg_dwell_time_ms']
corr_matrix = master_numeric[corr_features].corr()

# 6. Plot the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, vmin=-1, vmax=1)

plt.title('Correlation Matrix of Core Numeric Features', fontsize=14)
plt.tight_layout()
plt.show()