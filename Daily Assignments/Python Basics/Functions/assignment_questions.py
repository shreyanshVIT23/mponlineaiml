# 16. Recursive Function to Calculate Power (a^b)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)


# 17. Generate Pascal's Triangle
def pascal_triangle(rows):
    for i in range(rows):
        num = 1

        for j in range(rows - i):
            print(" ", end="")

        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)

        print()


# 18. Calculator Using Functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return "Cannot divide by zero" if b == 0 else a / b


# 19. Check String Palindrome
def is_string_palindrome(text):
    return text == text[::-1]


# 20. Count Uppercase, Lowercase, Digits and Symbols
def count_characters(text):
    upper = lower = digits = symbols = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        else:
            symbols += 1

    return upper, lower, digits, symbols


# 21. Remove Duplicate Elements from List
def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result


# 22. Recursive Fibonacci Function
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# 23. Decimal to Binary Conversion
def decimal_to_binary(num):
    if num == 0:
        return "0"

    binary = ""

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    return binary


# 24. Merge Two Sorted Lists
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


# 25. Find Second Largest Number in List
def second_largest(lst):
    largest = second = float("-inf")

    for num in lst:
        if num > largest:
            second = largest
            largest = num

        elif largest > num > second:
            second = num

    return second


# 26. Check Whether Two Strings Are Anagrams
def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())


# 27. Calculate Simple and Compound Interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal


# 28. Generate Prime Numbers Between Two Limits
def primes_between(start, end):
    primes = []

    for num in range(max(2, start), end + 1):
        is_prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


# 29. Menu-Driven Banking System
balance = 10000


def check_balance():
    print("Balance =", balance)


def deposit(amount):
    global balance
    balance += amount


def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")


# 30. Student Result Processing System
def process_result(marks):

    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return total, percentage, grade
