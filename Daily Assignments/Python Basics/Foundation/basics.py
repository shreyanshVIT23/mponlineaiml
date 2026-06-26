import math

# Question 1

name = "Shreyansh Pande"
age = 19

print("Name:", name)
print("Age:", age)

# Question 2

product_name = "Laptop"
quantity = 5
price = 65000.0

print("Product:", product_name)
print("Quantity:", quantity)
print("Price:", price)

# Question 3

## Method 1
a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)

## Method 2
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

# Question 4

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Third fruit:", fruits[2])

# Question 5


radius = float(input("Enter radius: "))

area = math.pi * radius**2

print("Area of circle =", area)

# Question 6

value = input("Enter any value: ")

print("Value:", value)
print("Data Type:", type(value))

# Question 7

student = {
    "name": "Christopher",
    "age": 20,
    "course": "Computer Science",
    "semester": 5,
    "cgpa": 8.9,
}

print(student)

## Accessing Individual Student Values

print("Name:", student["name"])
print("Course:", student["course"])
