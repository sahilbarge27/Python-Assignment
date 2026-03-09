import math

# Dataset
dataset = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# Accept user input
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

distances = []

# Step 1: Calculate Euclidean Distance
for point in dataset:
    name, px, py, label = point
    distance = math.sqrt((x - px)*2 + (y - py)*2)
    distances.append((name, distance, label))

# Step 2: Sort distances
distances.sort(key=lambda d: d[1])

# Step 3: Select K nearest neighbors
K = 3
neighbors = distances[:K]

print("\nNearest Neighbors:")

for n in neighbors:
    print(n[0], "- Distance:", round(n[1], 2))

# Step 4: Majority Voting
red = 0
blue = 0

for n in neighbors:
    if n[2] == "Red":
        red += 1
    else:
        blue += 1

# Step 5: Predict class
if red > blue:
    prediction = "Red"
else:
    prediction = "Blue"

print("\nPredicted Class:", prediction)