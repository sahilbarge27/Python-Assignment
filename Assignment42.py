
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

# Given regression parameters from Question 1
m = 0.4
c = 2.4

predicted_y = []

print("Predicted Y values:")
for x in X:
    y_pred = m*x + c
    predicted_y.append(y_pred)
    print("X =",x," Predicted Y =",round(y_pred,2))

# -------------------------
# Mean Squared Error (MSE)
# -------------------------

n = len(Y)
mse_sum = 0

for i in range(n):
    error = Y[i] - predicted_y[i]
    mse_sum = mse_sum + error**2

mse = mse_sum / n

print("\nMean Squared Error (MSE) =",round(mse,3))

# -------------------------
# R² Score
# -------------------------

mean_y = sum(Y)/n

ss_total = 0
ss_residual = 0

for i in range(n):
    ss_total += (Y[i] - mean_y)**2
    ss_residual += (Y[i] - predicted_y[i])**2

r2 = 1 - (ss_residual/ss_total)

print("R² Score =",round(r2,3))