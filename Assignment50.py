##########################################
# Step 1: Import Libraries
##########################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

##########################################
# Step 2: Load Dataset
##########################################
df = pd.read_csv("data.csv")   # replace with your dataset file

print("First 5 rows:")
print(df.head())

##########################################
# Handle missing / unknown values
##########################################
df.replace("unknown", np.nan, inplace=True)
df.dropna(inplace=True)

##########################################
# Basic stats
##########################################
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

##########################################
# Class Distribution
##########################################
target_column = df.columns[-1]   # assuming last column is target
sns.countplot(x=df[target_column])
plt.title("Class Distribution")
plt.show()

##########################################
# Step 3: Preprocessing
##########################################
le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

##########################################
# Split features & target
##########################################
X = df.drop(target_column, axis=1)
y = df[target_column]

##########################################
# Feature Scaling
##########################################
scaler = StandardScaler()
X = scaler.fit_transform(X)

##########################################
# Step 4: Train-Test Split
##########################################
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

##########################################
# Step 5: Train Models
##########################################
models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier()
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    
    print(f"\n{name} Results:")
    print("Accuracy:", acc)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

##########################################
# ROC-AUC (only for binary classification)
##########################################
for name, model in models.items():
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, y_prob)
        print(f"{name} ROC-AUC:", auc)

##########################################
# Step 6: Visualization
##########################################
# Confusion Matrix Plot (for Random Forest)
cm = confusion_matrix(y_test, models["Random Forest"].predict(X_test))

sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix - Random Forest")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

##########################################
# ROC Curve
##########################################
for name, model in models.items():
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        plt.plot(fpr, tpr, label=name)

plt.plot([0, 1], [0, 1], linestyle='--')
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()