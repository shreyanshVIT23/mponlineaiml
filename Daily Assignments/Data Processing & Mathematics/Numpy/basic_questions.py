import numpy as np

# 1. Create a NumPy array from a list
arr1 = np.array([10, 20, 30, 40, 50])
print("1. Array from List:")
print(arr1)

# 2. Create arrays using zeros(), ones(), and eye()
zeros_arr = np.zeros((3, 3))
ones_arr = np.ones((2, 4))
identity_arr = np.eye(4)

print("\n2. Zeros Array:")
print(zeros_arr)

print("\nOnes Array:")
print(ones_arr)

print("\nIdentity Matrix:")
print(identity_arr)

# 3. Find shape, size, and dimensions of an array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("\n3. Array:")
print(arr2)

print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Dimensions:", arr2.ndim)

# 4. Perform addition and subtraction on arrays
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\n4. Array Addition:")
print(a + b)

print("\nArray Subtraction:")
print(a - b)

# 5. Reshape a 1D array into a 2D array
arr3 = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr3.reshape(2, 3)

print("\n5. Original 1D Array:")
print(arr3)

print("\nReshaped 2D Array:")
print(reshaped)
