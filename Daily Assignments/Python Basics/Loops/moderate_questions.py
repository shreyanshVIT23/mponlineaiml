# 6. Find factorial using loops
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)

# 7. Check if number is Prime
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")

else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# 8. Reverse a number
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number =", reverse)

# 9. Check palindrome number
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# 10. Print fibonacci series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 11. Calculate GCD of 2 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD =", num1)

# 12. Check armstrong number
num = int(input("Enter a number: "))

original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit**digits
    num //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# 13. Print all prime number between 1 to 100
for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

# 14. Calculate sum of digits of a number
num = int(input("Enter a number: "))

total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum of Digits =", total)

# 15. Convert decimal number to binary
num = int(input("Enter decimal number: "))

binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print("Binary =", binary)
