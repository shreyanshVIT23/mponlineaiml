import numpy as np

# 6. Find Maximum, Minimum, and Mean of an Array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Mean:", np.mean(arr))


# 7. Create Multiplication Table Using NumPy Arrays
num = 5

table = np.arange(1, 11) * num

print("\nMultiplication Table of", num)
print(table)


# 8. Find Transpose of a Matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])

transpose = matrix.T

print("\nOriginal Matrix:")
print(matrix)

print("\nTranspose:")
print(transpose)


# 9. Generate Random Integers Using NumPy
random_numbers = np.random.randint(1, 101, size=10)

print("\nRandom Integers:")
print(random_numbers)


# 10. Perform Matrix Multiplication
A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

result = np.matmul(A, B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Multiplication:")
print(result)


# 11. Create Checkerboard Pattern Using NumPy
checkerboard = np.zeros((8, 8), dtype=int)

checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1

print("\nCheckerboard Pattern:")
print(checkerboard)


# 12. Split and Concatenate Arrays
arr = np.array([1, 2, 3, 4, 5, 6])

split_arrays = np.split(arr, 3)

print("\nSplit Arrays:")
print(split_arrays)

concatenated = np.concatenate(split_arrays)

print("\nConcatenated Array:")
print(concatenated)


# 13. Find Even Numbers from an Array
arr = np.array([10, 15, 20, 25, 30, 35, 40])

even_numbers = arr[arr % 2 == 0]

print("\nEven Numbers:")
print(even_numbers)


# 14. Replace All Odd Numbers with -1
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

modified = arr.copy()
modified[modified % 2 != 0] = -1

print("\nOriginal Array:")
print(arr)

print("\nAfter Replacing Odd Numbers:")
print(modified)


# 15. Create Identity Matrix of Size 5x5
identity_matrix = np.eye(5)

print("\n5x5 Identity Matrix:")
print(identity_matrix)
