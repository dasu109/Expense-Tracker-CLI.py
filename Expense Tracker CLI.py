import os
from datetime import datetime

FILE_PATH = "expenses.txt"

# ---------------------- Load Expenses ----------------------
def load_expenses():
    expenses = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            for line in file:
                date, desc, amount = line.strip().split(" | ")
                expenses.append((date, desc, float(amount)))
    return expenses


# ---------------------- Save Expenses ----------------------
def save_expenses(expenses):
    with open(FILE_PATH, "w") as file:
        for date, desc, amount in expenses:
            file.write(f"{date} | {desc} | {amount}\n")


# ---------------------- Add Expense ----------------------
def add_expense():
    desc = input("Enter description: ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    expenses = load_expenses()
    expenses.append((date, desc, amount))
    save_expenses(expenses)

    print("Expense added successfully!\n")


# ---------------------- View Expenses ----------------------
def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n--- Your Expenses ---")
    for i, (date, desc, amount) in enumerate(expenses, start=1):
        print(f"{i}. {date} | {desc} | ₹{amount}")
    print()


# ---------------------- Delete Expense ----------------------
def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to delete.\n")
        return

    view_expenses()
    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(expenses):
        deleted = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted: {deleted[1]} (₹{deleted[2]})\n")
    else:
        print("Invalid number.\n")


# ---------------------- Total Spending ----------------------
def total_spending():
    expenses = load_expenses()
    total = sum(amount for _, _, amount in expenses)
    print(f"\nTotal Spending: ₹{total}\n")


# ---------------------- Main Menu ----------------------
def menu():
    while True:
        print("===== Expense Tracker CLI =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Spending")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_spending()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    menu()
