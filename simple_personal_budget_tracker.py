income = 0
expenses = 0

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter income: "))
        income += amount
    elif choice == "2":
        amount = float(input("Enter expense: "))
        expenses += amount
    elif choice == "3":
        print(f"\nTotal Income: {income}")
        print(f"Total Expenses: {expenses}")
        print(f"Balance: {income - expenses}")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
