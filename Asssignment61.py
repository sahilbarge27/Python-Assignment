# ---------------------------------------------------
# Import Required Libraries
# ---------------------------------------------------

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# ---------------------------------------------------
# Load / Create Dataset
# Features:
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]
# ---------------------------------------------------

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

# Output:
# 0 = Customer will stay
# 1 = Customer will leave

y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])

# ---------------------------------------------------
# Clean Dataset
# ---------------------------------------------------

print("Checking Missing Values:")
print(np.isnan(X).sum())

# ---------------------------------------------------
# Split Dataset into Training and Testing
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------
# Apply StandardScaler
# ---------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ---------------------------------------------------
# Create FNN (Feed Forward Neural Network) Model
# ---------------------------------------------------

model = Sequential()

# Input Layer + Hidden Layer
model.add(Dense(8, activation='relu', input_shape=(5,)))

# Second Hidden Layer
model.add(Dense(4, activation='relu'))

# Output Layer
model.add(Dense(1, activation='sigmoid'))

# ---------------------------------------------------
# Compile Model
# ---------------------------------------------------

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ---------------------------------------------------
# Train FNN Model
# ---------------------------------------------------

model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=2,
    verbose=1
)

# ---------------------------------------------------
# Predict on Test Data
# ---------------------------------------------------

y_pred = model.predict(X_test)

# Convert probabilities into 0 or 1
y_pred = (y_pred > 0.5).astype(int)

# ---------------------------------------------------
# Evaluate Accuracy
# ---------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy * 100, "%")

# ---------------------------------------------------
# Test with New Customer Input
# ---------------------------------------------------

# [Age, Monthly Charges, Tenure, Complaints, Support Calls]

new_customer = np.array([[40, 1200, 10, 3, 5]])

# Apply Scaling
new_customer = scaler.transform(new_customer)

# Predict
prediction = model.predict(new_customer)

print("\nPrediction Value:", prediction)

if prediction > 0.5:
    print("Customer will leave")
else:
    print("Customer will stay")