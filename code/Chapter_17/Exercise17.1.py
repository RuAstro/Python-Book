import numpy as np

A = np.array([[3, 4, 5], [6, 7, 8], [9, 10, 11]])
# Calculate min, max and mean
min = np.min(A)
max = np.max(A)
mean = np.mean(A)

B = A**2

C = np.vstack((A, B))

result = C @ A

C_reshaped = np.reshape(C, (3, 3, 2))

print("Min value in A:", min)
print("Max value in A:", max)
print("Mean of all entries in A:", mean)

print("Array B (squared entries of A):\n", B)

print("Array C (stacked A on top of B):\n", C)

print("Matrix product of C by A:\n", result)

print("Reshaped array C:\n", C_reshaped)
