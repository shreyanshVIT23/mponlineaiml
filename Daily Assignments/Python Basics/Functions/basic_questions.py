# 1. Square of number
def square(num):
    return num * num


number = int(input("Enter a number: "))
print("Square =", square(number))


# 2. Check even or odd
def check_even_odd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))
print(check_even_odd(number))


# 3. Calculate factorial
def factorial(num):

    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact


number = int(input("Enter a number: "))
print("Factorial =", factorial(number))


# 4. Find largest of three number
def largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest =", largest(x, y, z))


# 5. Calculate sum of digits
def sum_of_digits(num):

    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total


number = int(input("Enter a number: "))
print("Sum of Digits =", sum_of_digits(number))
