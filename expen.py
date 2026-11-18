expenses = {}

def add_expense(category, amount):
    expenses[category] = expenses.get(category, 0) + amount
    print("Expense added successfully!")

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpense Details:")
    for category, amount in expenses.items():
        print(category, ":", amount)

    print("Total Expense:", sum(expenses.values()))


while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        add_expense(category, amount)

    elif choice == '2':
        show_expenses()

    elif choice == '3':
        print("Thank you!")
        break

    else:
        print("Invalid choice!")