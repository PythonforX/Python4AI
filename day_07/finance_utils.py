import json

transactions = []

def display_menu():
    print("\n Personal Fianance Manager!")
    print("1. Add a new Transaction")
    print("2. View Transaction")
    print("3. View Summary")
    print("4. Search for a Transaction")
    print("5. Save Data to a File")
    print("6. Load Data from a File")
    print("7. Exit")

def add_transaction():
    date = input("Enter date in (YYYY-MM-DD) : ")
    description = input("Description : ")
    amount = float(input("Enter amount : "))
    type_ = input("Type (income/expense) : ").lower()

    single_transaction = {
        'date' : date,
        'description' : description,
        'amount' : amount,
        'type' : type_
    }

    transactions.append(single_transaction)

def view_transaction():
    start_date = input("Enter start date (YYYY-MM-DD) or press Enter to view all : ")
    end_date = input("Enter end date (YYYY-MM-DD) or press Enter to view all")

    for transantion in transactions:
        if start_date and end_date:
            if start_date <= transantion['date'] <= end_date:
                print(transantion)
        
        else:
            print(transantion)

def view_summary():
    total_income = sum(t['amount'] for t in transactions if t['type']=="income")

    total_expense = sum(t['amount'] for t in transactions if t['type']=='expense')

    total_savings = total_income - total_expense

    print("----Summary----")
    print(f"Total Income : {total_income} /-")
    print(f"Total expense : {total_expense} /-")
    print(f"Net Savings : {total_savings} /-")

def search_transanctions():
    user_input = input("Enter description or amount of the transanction : ")

    for transaction in transactions:
        if user_input.lower() in transaction['description'].lower() or user_input.lower() in str(transaction['amount']):
            print(transaction)

def save_data():
    file_name = input("Enter the name of file : ")

    with open(file_name, 'a') as file:
        json.dump(transactions, file, indent = 4)

    print("Data saved successfully")

def load_data():
    file_name = input("Enter the filename to load data : ")

    with open(file_name, 'r') as file:
        global transactions
        transactions = json.load(file)

    print("Data loaded successfully")
