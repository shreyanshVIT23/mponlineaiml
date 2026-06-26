import math

print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        radius = float(input("Enter radius: "))
        area = math.pi * radius**2
        print("Area =", area)

    case 2:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        area = length * breadth
        print("Area =", area)

    case 3:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area =", area)

    case _:
        print("Invalid Choice")
