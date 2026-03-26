# ==========================================
# 1. Mean using NumPy
# ==========================================
import numpy as np

data = [6, 7, 8, 9, 10, 11, 12]

mean_value = np.mean(data)
print("Mean:", mean_value)


# ==========================================
# 2. Variance and Standard Deviation
# ==========================================
variance = np.var(data)
std_dev = np.std(data)

print("Variance:", variance)
print("Standard Deviation:", std_dev)


# ==========================================
# 3. Feature Scaling using StandardScaler
# ==========================================
from sklearn.preprocessing import StandardScaler

dataset = [[25, 20000],
           [30, 40000],
           [35, 80000]]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(dataset)

print("Scaled Dataset:")
print(scaled_data)


# ==========================================
# 4. Euclidean Distance before & after scaling
# ==========================================
from scipy.spatial.distance import euclidean

point1 = dataset[0]
point2 = dataset[1]

# Before scaling
distance_before = euclidean(point1, point2)

# After scaling
scaled_point1 = scaled_data[0]
scaled_point2 = scaled_data[1]
distance_after = euclidean(scaled_point1, scaled_point2)

print("Euclidean Distance before scaling:", distance_before)
print("Euclidean Distance after scaling:", distance_after)

print("\nExplanation:")
print("Before scaling, distance is dominated by large values (e.g., salary).")
print("After scaling, all features contribute equally.")


# ==========================================
# 5. Classification Report Concept
# ==========================================
print("\nClassification Report:")
print("A classification report is used to evaluate classification models.")
print("It shows metrics like Precision, Recall, F1-score, and Accuracy.")
print("It is mainly used in supervised classification models.")


# ==========================================
# 6. Metrics Explanation
# ==========================================
print("\nMetrics Meaning:")
print("Precision: Correct positive predictions / Total predicted positives")
print("Recall: Correct positive predictions / Total actual positives")
print("F1 Score: Harmonic mean of Precision and Recall")
print("Support: Number of actual occurrences of each class")
print("Accuracy: Correct predictions / Total predictions")


# ==========================================
# 7. Confusion Matrix Values
# ==========================================
actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

TP = TN = FP = FN = 0

for a, p in zip(actual, predicted):
    if a == 1 and p == 1:
        TP += 1
    elif a == 0 and p == 0:
        TN += 1
    elif a == 0 and p == 1:
        FP += 1
    elif a == 1 and p == 0:
        FN += 1

print("\nConfusion Matrix Values:")
print("True Positive (TP):", TP)
print("True Negative (TN):", TN)
print("False Positive (FP):", FP)
print("False Negative (FN):", FN)