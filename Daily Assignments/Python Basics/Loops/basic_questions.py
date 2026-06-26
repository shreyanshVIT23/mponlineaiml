# 1. Print numbers from 1 to 100
for i in range(1, 101):
    print(i)

# 2. Print even number between 2 and 50
for i in range(2, 51, 2):
    print(i)

# 3. Find sum of first n natural numbers
n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

# 4. Print multiplication table for a number
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 5. Count digits in a number
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits =", count)
