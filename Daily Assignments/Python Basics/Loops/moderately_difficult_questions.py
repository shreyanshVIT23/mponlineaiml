# 21. Check Strong number

import random
import math

num = int(input("Enter a number: "))
original = num
total = 0

while num > 0:
    digit = num % 10
    total += math.factorial(digit)
    num //= 10

if total == original:
    print("Strong Number")
else:
    print("Not a Strong Number")

# 22. Generate first n perfect numbers
n = int(input("How many perfect numbers? "))

count = 0
num = 1

while count < n:
    divisor_sum = 0

    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    if divisor_sum == num:
        print(num)
        count += 1

    num += 1

# 23. ATM Transactions
balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        balance += amount
        print("Updated Balance =", balance)

    elif choice == 3:
        amount = float(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Updated Balance =", balance)
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")

# 24. Menu driven calc using loops
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid Choice")

# 25. Frequency of digits in a number
num = input("Enter a number: ")

frequency = {}

for digit in num:
    if digit in frequency:
        frequency[digit] += 1
    else:
        frequency[digit] = 1

print(frequency)

# 26. Sort numbers without using Sort
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

# 27. Find second largest element in list
numbers = [10, 50, 20, 80, 40]

largest = second = float("-inf")

for num in numbers:
    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print("Second Largest =", second)

# 28. Generate all factors of a number

num = int(input("Enter a number: "))

print("Factors:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

# 29. Print multiplication table from 1 to 10
for num in range(1, 11):
    print("\nTable of", num)

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# 30. Number guessing game using loops

secret = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess < secret:
        print("Too Small")

    elif guess > secret:
        print("Too Large")

    else:
        print("Congratulations! You guessed correctly.")
        break

# 31. Check if string is palindrome
text = input("Enter a string: ")

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

if text == reversed_text:
    print("Palindrome")
else:
    print("Not a Palindrome")

# 32. Count vowels, consonants, and spaces in string
text = input("Enter a string: ")

vowels = consonants = digits = spaces = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

    elif char.isdigit():
        digits += 1

    elif char == " ":
        spaces += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)

# 33. Generate Patterns using alphabets
rows = 5

for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()

rows = 5
ch = 65

for i in range(rows):
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()

# 34. LCM of 2 number using loops
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

greater = max(num1, num2)

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break

    greater += 1

print("LCM =", lcm)

# 35. Login auth with 3 attempts
correct_username = "admin"
correct_password = "python123"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break

    else:
        attempts += 1
        print("Invalid Credentials")
        print("Attempts Left:", 3 - attempts)

else:
    print("Account Locked")
