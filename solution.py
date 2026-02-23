print("ATM Machine")

balance = 1000

choice = int(input("1. Withdraw  2. Deposit: "))

if choice == 1:
    amount = int(input("Enter withdraw amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdraw successful")
    else:
        print("Insufficient balance")

elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Deposit successful")

else:
    print("Invalid choice")

print("Current Balance:", balance)

if balance < 500:
    print("Low balance warning")
else:
    print("Balance sufficient")