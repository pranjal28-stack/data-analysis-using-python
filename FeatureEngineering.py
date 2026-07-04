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

print("=== Starting Feature Engineering ===")

# 1. Base user profiles
final_df = users[['user_id', 'age', 'income_level', 'loyalty_tier']].copy()

# 2. Add Total Spending & Total Transactions
spend_stats = purchases.groupby('user_id').agg(
    total_spent=('total_amount', 'sum'),
    total_transactions=('purchase_id', 'count')
).reset_index()
final_df = final_df.merge(spend_stats, on='user_id', how='left')

# 3. Add Session Counts & Conversion Success
session_stats = sessions.groupby('user_id').agg(
    total_sessions=('session_id', 'count'),
    converted_sessions=('is_converted', 'sum')
).reset_index()
final_df = final_df.merge(session_stats, on='user_id', how='left')

# 4. Add Behavioral Interaction Dwell Time
interaction_stats = interactions.groupby('user_id')['dwell_time_ms'].mean().reset_index(name='avg_dwell_time_seconds')
interaction_stats['avg_dwell_time_seconds'] = interaction_stats['avg_dwell_time_seconds'] / 1000
final_df = final_df.merge(interaction_stats, on='user_id', how='left')

# 5. Clean up blanks for users who browsed but never bought/converted
final_df['total_spent'] = final_df['total_spent'].fillna(0)
final_df['total_transactions'] = final_df['total_transactions'].fillna(0)
final_df['total_sessions'] = final_df['total_sessions'].fillna(0)
final_df['converted_sessions'] = final_df['converted_sessions'].fillna(0)
final_df['avg_dwell_time_seconds'] = final_df['avg_dwell_time_seconds'].fillna(0)

print("\n=== Feature Engineered Dataset Preview ===")
print(final_df.head())

# Save it to a CSV so it's ready for your model script!
final_df.to_csv('model_ready_users.csv', index=False)
print("\nSuccess! Saved to 'model_ready_users.csv'")