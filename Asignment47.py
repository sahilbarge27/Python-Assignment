# ==========================================
# 1. Concept of Variance (Explanation)
# ==========================================
print("Variance measures how much the data points spread out from the mean.")
print("It tells us whether the data is tightly clustered or widely spread.")
print("It is important in data analysis and ML to understand data distribution.\n")


# ==========================================
# 2. Step-by-step Variance Calculation
# Dataset: 4, 6, 8, 10, 12
# ==========================================
data1 = [4, 6, 8, 10, 12]

# Mean
mean1 = sum(data1) / len(data1)
print("Mean:", mean1)

# Deviation from mean
deviations = [x - mean1 for x in data1]
print("Deviations:", deviations)

# Square of deviations
squared_deviations = [d**2 for d in deviations]
print("Squared Deviations:", squared_deviations)

# Variance
variance1 = sum(squared_deviations) / len(data1)
print("Variance:", variance1, "\n")


# ==========================================
# 3. Standard Deviation Concept
# ==========================================
print("Standard deviation is the square root of variance.")
print("It tells how much data deviates from the mean in original units.\n")


# ==========================================
# 4. Calculations for dataset: 5, 7, 9, 11, 13
# ==========================================
import math

data2 = [5, 7, 9, 11, 13]

# Mean
mean2 = sum(data2) / len(data2)

# Variance
variance2 = sum((x - mean2) ** 2 for x in data2) / len(data2)

# Standard deviation
std_dev2 = math.sqrt(variance2)

print("Dataset:", data2)
print("Mean:", mean2)
print("Variance:", variance2)
print("Standard Deviation:", std_dev2, "\n")


# ==========================================
# 5. Feature Scaling Concept
# ==========================================
print("Feature scaling ensures all features have similar scale.")
print("It improves performance of ML models like KNN, SVM, Gradient Descent.\n")


# ==========================================
# 6. Standard Scaling Explanation
# ==========================================
print("Standard Scaling transforms data so that:")
print("Mean becomes 0 and Standard Deviation becomes 1.\n")


# ==========================================
# 7. Standard Scaling Calculation
# Dataset: mean = 9, std = 2
# Values: 6, 9, 12
# Formula: (x - mean) / std
# ==========================================
mean = 9
std = 2

values = [6, 9, 12]

scaled_values = [(x - mean) / std for x in values]

print("Original Values:", values)
print("Scaled Values:", scaled_values)