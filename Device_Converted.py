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
# 1. Calculate the exact conversion percentage for each device type
device_conversion = sessions.groupby('device_type')['is_converted'].mean() * 100
print("=== Conversion Rate by Device ===")
print(device_conversion.round(2).apply(lambda x: f"{x}%"))

# 2. Visualize it with a clean bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x=device_conversion.index, y=device_conversion.values, palette='Blues_d',
            order=device_conversion.sort_values(ascending=False).index)

plt.title('Conversion Rate (%) by Device Type', fontsize=14)
plt.xlabel('Device Type', fontsize=12)
plt.ylabel('Conversion Rate (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()