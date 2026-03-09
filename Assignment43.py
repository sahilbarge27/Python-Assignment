import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Original Dataset")
print(data)

# Step 2: Encode categorical values
le = LabelEncoder()

data['Weather'] = le.fit_transform(data['Weather'])
data['Temperature'] = le.fit_transform(data['Temperature'])
data['Play'] = le.fit_transform(data['Play'])

print("\nEncoded Dataset")
print(data)

# Step 3: Separate features and target
X = data[['Weather','Temperature']]
y = data['Play']

# Step 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
X,y,test_size=0.2,random_state=42)

# Step 5: Train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

# Step 6: Test prediction
test_data = [[2,0]]   # Sunny,Cool
prediction = model.predict(test_data)

if prediction == 1:
    print("\nPrediction : Yes (Play)")
else:
    print("\nPrediction : No (Don't Play)")

# Step 7: Accuracy
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print("\nModel Accuracy:",accuracy*100,"%"