salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 10:
    bonus = salary * 0.10
elif years >= 6:
    bonus = salary * 0.08
elif years >= 3:
    bonus = salary * 0.05
else:
    bonus = 0

print("Bonus = ₹", bonus)
