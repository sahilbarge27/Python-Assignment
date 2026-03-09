import math

# Dataset
dataset = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]

# Step 1: User input
study = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

distances = []

# Step 2: Calculate Euclidean Distance
for data in dataset:
    hours, attend, result = data
    distance = math.sqrt((study - hours)*2 + (attendance - attend)*2)
    distances.append((distance, result))

# Step 3: Sort distances
distances.sort()

# Step 4: Select K nearest neighbors
K = 3
neighbors = distances[:K]

pass_count = 0
fail_count = 0

# Step 5: Majority voting
for n in neighbors:
    if n[1] == "Pass":
        pass_count += 1
    else:
        fail_count += 1

# Step 6: Prediction
if pass_count > fail_count:
    prediction = "Pass"
else:
    prediction = "Fail"

print("\nPredicted Result:", prediction).