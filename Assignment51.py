##########################################
# Step 1: Import Libraries
##########################################
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt
import seaborn as sns

##########################################
# Step 2: Load Dataset
##########################################
# Load both CSV files
fake = pd.read_csv("fake.csv")
true = pd.read_csv("true.csv")

# Add labels
fake["label"] = 0   # Fake
true["label"] = 1   # Real

# Combine datasets
df = pd.concat([fake, true], axis=0)

##########################################
# Step 3: Data Preprocessing
##########################################
# Drop null values
df.dropna(inplace=True)

# Use only 'text' column (or you can use 'title')
df = df[["text", "label"]]

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

##########################################
# Step 4: Feature Extraction (TF-IDF)
##########################################
tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)

X = tfidf.fit_transform(df["text"])
y = df["label"]

##########################################
# Step 5: Train-Test Split
##########################################
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

##########################################
# Step 6: Train Individual Models
##########################################
lr = LogisticRegression()
dt = DecisionTreeClassifier()

lr.fit(X_train, y_train)
dt.fit(X_train, y_train)

##########################################
# Step 7: Voting Classifier
##########################################
# Hard Voting
hard_voting = VotingClassifier(
    estimators=[("lr", lr), ("dt", dt)],
    voting='hard'
)

# Soft Voting
soft_voting = VotingClassifier(
    estimators=[("lr", lr), ("dt", dt)],
    voting='soft'
)

hard_voting.fit(X_train, y_train)
soft_voting.fit(X_train, y_train)

##########################################
# Step 8: Evaluation Function
##########################################
def evaluate_model(name, model):
    y_pred = model.predict(X_test)
    
    print(f"\n{name} Results:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    # Plot confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title(f"{name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

##########################################
# Step 9: Compare All Models
##########################################
evaluate_model("Logistic Regression", lr)
evaluate_model("Decision Tree", dt)
evaluate_model("Hard Voting", hard_voting)
evaluate_model("Soft Voting", soft_voting)