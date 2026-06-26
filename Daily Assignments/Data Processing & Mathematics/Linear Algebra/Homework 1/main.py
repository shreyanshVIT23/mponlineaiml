import numpy as np

# 1. Vector Operations

vector1 = np.array([2, 4, 6])
vector2 = np.array([1, 3, 5])

print("Vector 1:", vector1)
print("Vector 2:", vector2)

# Addition
print("\nAddition:")
print(vector1 + vector2)

# Subtraction
print("\nSubtraction:")
print(vector1 - vector2)

# Dot Product
print("\nDot Product:")
print(np.dot(vector1, vector2))


# 2. Matrix Multiplication by Scalar

matrix = np.array([[2, 3], [4, 5]])

print("\nOriginal Matrix:")
print(matrix)

print("\nMatrix × 3:")
print(matrix * 3)


# 3. Find Shape of Matrix

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("\nArray:")
print(arr)

print("Shape:", arr.shape)


# 4. Feature Matrix

feature_matrix = np.array([[22, 1], [25, 3], [30, 5]])

print("\nFeature Matrix (Age, Experience):")
print(feature_matrix)

print("Shape:", feature_matrix.shape)
