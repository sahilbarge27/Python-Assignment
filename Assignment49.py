# ==========================================
# 1. Exploratory Data Analysis (EDA)
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (change filename if needed)
df = pd.read_csv("diabetes.csv")

# Display first 5 rows
print("First 5 rows:\n", df.head())

# Column info & null values
print("\nDataset Info:")
print(df.info())

print("\nNull values:\n", df.isnull().sum())

# Basic statistics
print("\nStatistical Summary:\n", df.describe())

# Distribution of target variable
plt.figure()
sns.countplot(x='Outcome', data=df)
plt.title("Distribution of Target Variable (Outcome)")
plt.show()

# Histograms
df.hist(figsize=(10, 8))
plt.show()

# Boxplot for outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.show()

# Pairplot
sns.pairplot(df, hue='Outcome')
plt.show()


# ==========================================
# 2. Data Preprocessing
# ==========================================
from sklearn.preprocessing import StandardScaler

# Replace 0 values with NaN in specific columns
cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols] = df[cols].replace(0, pd.NA)

# Fill missing values with mean
df.fillna(df.mean(), inplace=True)

# Features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ==========================================
# 3. Model Building
# ==========================================
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Models
models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier()
}

trained_models = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    trained_models[name] = model


# ==========================================
# 4. Model Evaluation
# ==========================================
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

for name, model in trained_models.items():
    print(f"\n===== {name} =====")
    
    y_pred = model.predict(X_test)
    
    # Accuracy
    print("Accuracy:", accuracy_score(y_test, y_pred))
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)
    
    # Classification Report
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    # Visualization
    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title(f"{name} - Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()


# ==========================================
# 5. Final Output (Prediction)
# ==========================================
# Example test data (replace with your values)
sample = [[5, 120, 70, 20, 80, 25.0, 0.5, 30]]

# Scale input
sample_scaled = scaler.transform(sample)

# Predict using best model (example: Logistic Regression)
prediction = trained_models["Logistic Regression"].predict(sample_scaled)

print("\nPrediction (0 = No Diabetes, 1 = Diabetes):", prediction[0])


# Save predictions to CSV
output_df = pd.DataFrame({
    "Actual": y_test,
    "Predicted": trained_models["Logistic Regression"].predict(X_test)
})

output_df.to_csv("predictions.csv", index=False)
print("\nPredictions saved to predictions.csv")