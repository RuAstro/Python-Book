import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(2 * A)

B = np.array([[5, 4, 3], [7, 6, 5], [9, 8, 7]])
C = B - A
print(C)


A = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(A * A)

# calculate matrix product, use @ operator
print(A @ A)

# Get a tuple of axis length
print(matrix.shape)

# Get an array of the diagonal entries
print(matrix.diagonal())
array([1, 5, 9])

# Get a one-dimensional array of all entries
matrix.flatten()
array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Get the transpose of an array
matrix.transpose()
array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

# Calculate the minimum entry
matrix.min()
1

# Calculate the maximum entry
matrix.max()
9

# Calculate the average value of all entries
matrix.mean()
5.0
