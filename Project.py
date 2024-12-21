
categories = ["Food", "Transport", "Entertainment", "Utilities", "Miscellaneous"]
expenses = {category: 0.0 for category in categories} 
total_expenses = 0.0 

def display_summary():
    global total_expenses
    print("\n----- Expense Summary -----")
    for category, amount in expenses.items():
        percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
        print(f"{category}: ${amount:.2f} ({percentage:.2f}%)")
    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    print("---------------------------\n")

def add_expense():
    global total_expenses
    print("\nChoose a category to add an expense:")
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")
    
    try:
        category_choice = int(input("\nEnter the number of the category: ")) - 1
        if category_choice < 0 or category_choice >= len(categories):
            print("Invalid category choice.")
            return
        
        amount = float(input(f"Enter the amount spent on {categories[category_choice]}: $"))
        if amount < 0:
            print("Amount cannot be negative.")
            return
        
        category = categories[category_choice]
        expenses[category] += amount
        total_expenses += amount
        print(f"Added ${amount:.2f} to {category}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def run_expense_tracker():
    while True:
        print("\n----- Daily Expense Tracker -----")
        print("1. Add an expense")
        print("2. Show summary")
        print("3. Exit")
        
        try:
            choice = int(input("\nChoose an option (1, 2, or 3): "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                display_summary()
            elif choice == 3:
                print("Exiting the tracker. Have a great day!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if _name_ == "_main_":
    run_expense_tracker()
