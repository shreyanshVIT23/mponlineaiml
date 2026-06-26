units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 4)
else:
    bill = (100 * 2) + (100 * 4) + ((units - 200) * 6)

print("Electricity Bill = ₹", bill)
