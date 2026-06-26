# 6. Check Prime Number
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# 7. Generate Fibonacci Series
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()


# 8. Recursive Factorial
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


# 9. Reverse a Number
def reverse_number(num):
    reverse = 0

    while num > 0:
        reverse = reverse * 10 + (num % 10)
        num //= 10

    return reverse


# 10. Check Palindrome Number
def is_palindrome(num):
    return num == reverse_number(num)


# 11. Calculate GCD of Two Numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


# 12. Check Armstrong Number
def is_armstrong(num):
    digits = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit**digits
        temp //= 10

    return total == num


# 13. Count Vowels in a String
def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count


# 14. Find Frequency of Elements in a List
def frequency(lst):
    freq = {}

    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq


# 15. Sort List Without Using Built-in sort()
def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


# Example Usage

print("Prime:", is_prime(13))

print("Fibonacci Series:")
fibonacci(10)

print("Factorial:", factorial(5))

print("Reversed Number:", reverse_number(1234))

print("Palindrome:", is_palindrome(121))

print("GCD:", gcd(24, 36))

print("Armstrong:", is_armstrong(153))

print("Vowel Count:", count_vowels("Hello World"))

print("Frequency:", frequency([1, 2, 2, 3, 3, 3]))

print("Sorted List:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
