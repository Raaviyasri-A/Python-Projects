expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))

def show_expenses():
    total = 0
    for e in expenses:
        print(e[0], "-", e[1])
        total += e[1]
    print("Total:", total)

while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
