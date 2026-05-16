# Artificial Intelligence Project 2
# Data Classification Using AI
# DecodeLabs Internship Project

# Step 1: Import Required Libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 2: Load Dataset
iris = load_iris()

# Features (Input Data)
X = iris.data

# Labels (Output Categories)
y = iris.target

# Step 3: Split Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Step 4: Create Classification Model
model = DecisionTreeClassifier(random_state=42)

# Step 5: Train the Model
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("===================================")
print(" AI Classification Project")
print("===================================")

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Step 8: Show Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Step 9: Show Confusion Matrix
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# Step 10: Example Prediction
sample_data = [X_test[0]]

prediction = model.predict(sample_data)

print("\n===================================")
print(" Example Prediction")
print("===================================")

print("Predicted Flower Type:",
      iris.target_names[prediction][0])

# ===================================
# EXTRA IMPROVEMENTS ADDED
# ===================================

# 1. Random state added for reproducibility
# 2. Classification report added
# 3. Confusion matrix added
# 4. Clean professional formatting
# 5. Example prediction added

print("\nProject Completed Successfully!")