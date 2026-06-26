balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Balance = ₹", balance)

    case 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Updated Balance = ₹", balance)

    case 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Updated Balance = ₹", balance)
        else:
            print("Insufficient Balance")

    case _:
        print("Invalid Choice")
