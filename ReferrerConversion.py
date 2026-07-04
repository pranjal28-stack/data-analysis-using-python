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
# Calculate conversion rate per referrer source
referrer_conversion = sessions.groupby('referrer_source')['is_converted'].mean() * 100
referrer_conversion = referrer_conversion.sort_values(ascending=False)

print("=== Conversion Rate by Referrer Source ===")
print(referrer_conversion.round(2).apply(lambda x: f"{x}%"))

# Plot the results
plt.figure(figsize=(10, 5))
sns.barplot(x=referrer_conversion.values, y=referrer_conversion.index, palette='flare')

plt.title('Conversion Rate (%) by Referrer Source', fontsize=14)
plt.xlabel('Conversion Rate (%)', fontsize=12)
plt.ylabel('Referrer Source', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()