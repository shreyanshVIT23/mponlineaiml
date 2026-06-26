import numpy as np
import time

# 16. Create 5x5 Matrix and Find Statistics
matrix = np.random.randint(1, 101, (5, 5))

print("16. Random 5x5 Matrix")
print(matrix)

print("Maximum Value:", np.max(matrix))
print("Minimum Value:", np.min(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))


# 17. Matrix Addition, Subtraction and Multiplication
A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

print("\n17. Matrix Operations")

print("Addition:")
print(A + B)

print("Subtraction:")
print(A - B)

print("Multiplication:")
print(np.matmul(A, B))


# 18. Numbers from 1 to 100
arr = np.arange(1, 101)

primes = []

for num in arr:
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

even_numbers = arr[arr % 2 == 0]

print("\n18. Array Analysis")
print("Prime Numbers:")
print(primes)

print("Even Numbers:")
print(even_numbers)

print("Sum of Elements:", np.sum(arr))


# 19. Reshape 1D Array into Different Dimensions
arr = np.arange(1, 13)

print("\n19. Original Array")
print(arr)

print("\nShape (3,4)")
print(arr.reshape(3, 4))

print("\nShape (2,6)")
print(arr.reshape(2, 6))

print("\nShape (4,3)")
print(arr.reshape(4, 3))

# Condition:
# Product of dimensions must equal total elements.


# 20. Generate Identity, Upper and Lower Triangular Matrices
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\n20. Identity Matrix")
print(np.eye(3))

print("\nUpper Triangular Matrix")
print(np.triu(matrix))

print("\nLower Triangular Matrix")
print(np.tril(matrix))


# 21. Row-wise Sum, Column-wise Sum and Transpose
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\n21. Matrix")
print(matrix)

print("Row-wise Sum:")
print(np.sum(matrix, axis=1))

print("Column-wise Sum:")
print(np.sum(matrix, axis=0))

print("Transpose:")
print(matrix.T)


# 22. Image-like Matrix Operations
image = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print("\n22. Original Image Matrix")
print(image)

print("\nBrightness Increased")
print(image + 50)

print("\nImage Flipped Horizontally")
print(np.fliplr(image))

print("\nImage Flipped Vertically")
print(np.flipud(image))


# 23. Compare Python List vs NumPy Array Speed
size = 1000000

python_list = list(range(size))
numpy_array = np.arange(size)

start = time.time()
result = [x * 2 for x in python_list]
list_time = time.time() - start

start = time.time()
result = numpy_array * 2
numpy_time = time.time() - start

print("\n23. Speed Comparison")
print("Python List Time:", list_time)
print("NumPy Array Time:", numpy_time)


# 24. Repeated Matrix Multiplication
print("\n24. Repeated Matrix Multiplication")

for i in range(5):
    A = np.random.randint(1, 10, (3, 3))
    B = np.random.randint(1, 10, (3, 3))
    result = np.matmul(A, B)
    print(f"\nIteration {i + 1}")
    print(result)


# 25. Statistical Analysis Using NumPy
data = np.array([12, 15, 18, 20, 22, 25, 30, 35])

print("\n25. Statistical Analysis")

print("Data:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))
