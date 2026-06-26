# 16. Pyramid Pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# 17. Floyd's triangle
rows = int(input("Enter number of rows: "))

num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 18. Pascal's triangle

rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = 1

    print(" " * (rows - i), end="")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()

# 19. Inverted Pyramid
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

# 20. Hollow Square Pattern
size = int(input("Enter size: "))

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
