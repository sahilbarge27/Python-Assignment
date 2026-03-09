# Step 1 : Import Libraries

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# Step 2 : Load Dataset

data = pd.read_csv("PlayPredictor.csv")

print("Dataset is :")
print(data)


# Step 3 : Label Encoding (Convert text to numbers)

le_weather = LabelEncoder()
le_temp = LabelEncoder()
le_play = LabelEncoder()

data['Weather'] = le_weather.fit_transform(data['Weather'])
data['Temperature'] = le_temp.fit_transform(data['Temperature'])
data['Play'] = le_play.fit_transform(data['Play'])

print("\nEncoded Dataset :")
print(data)


# Step 4 : Separate Features and Target

X = data[['Weather', 'Temperature']]
Y = data['Play']


# Step 5 : Split Dataset into Training and Testing

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)


# Step 6 : Train KNN Model

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, Y_train)


# Step 7 : Testing Model

prediction = model.predict(X_test)

print("\nPredicted Output :")
print(prediction)

print("\nActual Output :")
print(Y_test.values)


# Step 8 : Calculate Accuracy

accuracy = accuracy_score(Y_test, prediction)

print("\nAccuracy of Model is :", accuracy * 100)