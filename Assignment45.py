# Step 1: Import required libraries
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 2: Get Data
wine = load_wine()

# Convert to DataFrame for better understanding
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target)

print("Feature Data:")
print(X.head())

print("\nTarget Data:")
print(y.head())

# Step 3: Clean, Prepare and Manipulate Data
# Split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Train Model
# Using KNN classifier
model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

# Step 5: Test Data
y_pred = model.predict(X_test)

# Step 6: Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))