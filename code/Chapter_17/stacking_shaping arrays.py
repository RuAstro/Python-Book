import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])


print(np.vstack([A, B]))
print(np.hstack)


# can also reshape arrays with np.reshape()
print(A.reshape(6, 1))


# So, np.arange(1, 10) returns an array containing the numbers 1 through 9.
matrix = nums.reshape(3, 3)
print(matrix)

# Do it in one line
np.arange(1, 10).reshape(3, 3)


# Create 3 imensional array using np.array() and np.reshape():
np.arange(1, 13).reshape(3, 2, 2)
