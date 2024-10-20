# -*- coding: utf-8 -*-
"""diabetes.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rGqdGSdy-jgk3jXqlcM6FVoOlnn7rrrT
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')

print("First few rows of the dataset:")
print(df.head())

print("\nDataset info:")
df.info()

print("\nDataset statistics:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

X = df.drop('Outcome', axis=1)
y = df['Outcome']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

y_proba = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
new_patient = [[6, 148, 72, 35, 0, 33.6, 0.627, 50]]  # Replace with actual feature values
new_patient_scaled = scaler.transform(new_patient)
prediction = model.predict(new_patient_scaled)
print("\nDiabetes prediction for new patient (1 = Positive, 0 = Negative):", prediction)