import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns



print("=== Initializing Model Training ===")

# 1. Load our feature engineered master dataset
df = pd.read_csv('model_ready_users.csv')

# 2. Define our Target Variable
# Let's predict if a user is a "High-Value Customer" (e.g., converted more than once)
df['is_high_value'] = (df['converted_sessions'] > 1).astype(int)

# 3. Separate features (X) and target (y)
# Drop IDs, targets, and columns used to create the target
X = df.drop(columns=['user_id', 'is_high_value', 'converted_sessions'])
y = df['is_high_value']

# 4. One-Hot Encode categorical text variables (income_level, loyalty_tier)
X = pd.get_dummies(X, columns=['income_level', 'loyalty_tier'], drop_first=True)

# 5. Split data into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 6. Scale numerical features
scaler = StandardScaler()
numerical_cols = ['age', 'total_spent', 'total_transactions', 'total_sessions', 'avg_dwell_time_seconds']
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

# 7. Train a Random Forest Classifier with Balanced Class Weights
print("Training Balanced Random Forest Model...")
model = RandomForestClassifier(random_state=42, n_estimators=100, class_weight='balanced')
model.fit(X_train, y_train)

# 8. Evaluate Model Performance
y_pred = model.predict(X_test)
print("\n=== Model Evaluation Report ===")
print(classification_report(y_test, y_pred))

# 9. Extract and Plot Feature Importances
importances = model.feature_importances_
feature_names = X.columns

# Create a clean DataFrame sorted by importance score
feat_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feat_imp_df = feat_imp_df.sort_values(by='Importance', ascending=False)

print("\n=== Feature Importance Rankings ===")
print(feat_imp_df)

# Plot it
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feat_imp_df, palette='viridis')
plt.title('What Drives High-Value Customers? (Feature Importances)', fontsize=14)
plt.xlabel('Importance Score', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.tight_layout()
plt.show()