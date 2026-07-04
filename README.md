# E-Commerce Predictive Analytics Pipeline

A complete end-to-end data science pipeline built in Python to explore, engineer, and predict high-value customer behavior using a multi-table relational e-commerce dataset.

## 📌 Project Overview
This repository contains a full machine learning pipeline designed to identify High-Value Customers (defined as users executing more than one conversion transaction). The system transitions seamlessly from raw relational data to Exploratory Data Analysis (EDA), feature engineering, data normalization, handling severe class imbalances, and training a robust ensemble classification model.

---

## 📊 Core Data Insights (EDA)
Through comprehensive single-table and multi-table analysis, several critical operational insights were discovered:
* Behavior Over Demographics: The model training revealed that static user demographics (age, income_level, loyalty_tier) have close to zero predictive power. Instead, behavioral features (total_transactions and total_spent) dictate 75%+ of the model's predictive capability.
* Uniform Conversion: Conversion rates remain remarkably uniform across both acquisition channels (~7.2% to 8.1%) and device types (~7.2% to 7.5%).
* Intent Capture: Page dwell time analysis perfectly captures user intent; highly active decision actions (view, add_to_cart) possess vast right-skewed attention tails, while transactional actions (click, remove_from_cart) exhibit instant, low-dwell distributions.

---

## 🛠️ Pipeline Architecture & Code Structure

The repository is organized into distinct standalone scripts representing different stages of the production pipeline:

### 1. Unified Dataset Construction (FeatureEngineering.py)
Flattens the relational layout (Users, Sessions, Interactions, Purchases, and Reviews) by aggregating metrics at a clean, singular user-level footprint.
* Computes overall purchase aggregates (total_spent, total_transactions).
* Computes session interaction densities (total_sessions, converted_sessions).
* Isolates attention span durations (avg_dwell_time_seconds).
* Handles structural data cleaning by resolving multi-table blanks (.fillna(0)) to prepare features for modeling.

### 2. Predictive Modeling Engine (TrainModel.py)
Loads the feature-engineered layout to train, evaluate, and extract feature hierarchies from the AI brain.
* One-Hot Encoding: Translates string categorical attributes (income_level, loyalty_tier) into mathematical binary vectors.
* Feature Scaling: Uses a StandardScaler to ensure numerical scales (e.g., age vs. dollar value) are uniformly weighted.
* Class Imbalance Mitigation: Combats severe lopsided boundaries (only 29 high-value users out of 2,000 cases) by applying an algorithmic class weight balancing parameter (class_weight='balanced').
* Algorithm: Implements a 100-tree Random Forest Ensemble Classifier.

---

## 📈 Model Performance & Evaluation

### Classification Metrics
By optimizing for class imbalances, the target class metrics were successfully prioritized:

=== Model Evaluation Report ===
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      1971
           1       0.68      0.45      0.54        29

    accuracy                           0.99      2000
   macro avg       0.84      0.72      0.77      2000
weighted avg       0.99      0.99      0.99      2000

* Precision (0.68): When the model flags a customer as high-value, it is accurate 68% of the time.
* Recall (0.45): The engine successfully intercepts 45% of total high-value users within highly sparse target profiles.

### Feature Importance Rankings

=== Feature Importance Rankings ===
                  Feature    Importance Score
0      total_transactions            0.530894
1             total_spent            0.244347
2          total_sessions            0.148758
3  avg_dwell_time_seconds            0.051036
4                     age            0.011917

---

## 🚀 How to Run the Pipeline

1. Ensure the raw CSV data splits are located in your active directory path.
2. Compile the aggregate model spreadsheet feature file:
   python FeatureEngineering.py
3. Execute the classification workflow, evaluate outputs, and review feature importance plotting curves:
   python TrainModel.py

## 🧰 Tech Stack
* Language: Python 3.13+
* Data Scrape & Compute: Pandas, NumPy
* Graphics Visualization: Matplotlib, Seaborn
* Machine Learning Engine: Scikit-Learn