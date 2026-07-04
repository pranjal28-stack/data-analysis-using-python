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


print('----Sessions Info-----')
print(sessions.info())
print('----Sessions Head-----')
print(sessions.head())


# Set up a grid of 3 subplots side-by-side
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Device Type Breakdown
sns.countplot(data=sessions, x='device_type', ax=axes[0], palette='pastel',
              order=sessions['device_type'].value_counts().index)
axes[0].set_title('Sessions by Device Type')
axes[0].set_xlabel('Device Type')
axes[0].set_ylabel('Number of Sessions')

# Plot 2: Referrer Source Breakdown
sns.countplot(data=sessions, x='referrer_source', ax=axes[1], palette='Set2',
              order=sessions['referrer_source'].value_counts().index)
axes[1].set_title('Sessions by Referrer Source')
axes[1].set_xlabel('Referrer Source')
axes[1].set_ylabel('Number of Sessions')
axes[1].tick_params(axis='x', rotation=45) # Rotate names if they overlap

# Plot 3: Conversion Rate Breakdown (True vs False)
sns.countplot(data=sessions, x='is_converted', ax=axes[2], palette='coolwarm')
axes[2].set_title('Session Conversion (Is Converted?)')
axes[2].set_xlabel('Converted')
axes[2].set_ylabel('Number of Sessions')

plt.tight_layout()
plt.show()
# Calculate the percentage of True values in the 'is_converted' column
conversion_rate = sessions['is_converted'].mean() * 100

print(f"Overall Session Conversion Rate: {conversion_rate:.2f}%")