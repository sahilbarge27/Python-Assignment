import math

# Dataset (same as Assignment 1)
dataset = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# User input
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

distances = []

# Step 1: Calculate Euclidean Distance
for data in dataset:
    name, px, py, label = data
    distance = math.sqrt((x - px)*2 + (y - py)*2)
    distances.append((name, distance, label))

# Step 2: Sort distances
distances.sort(key=lambda d: d[1])

print("\nPrediction Results")

# Step 3: Test for different K values
k_values = [1, 3, 5]

for K in k_values:

    neighbors = distances[:K]

    red = 0
    blue = 0

    for n in neighbors:
        if n[2] == "Red":
            red += 1
        else:
            blue += 1

    if red > blue:
        prediction = "Red"
    else:
        prediction = "Blue"

    print("K =", K, "->", prediction) 