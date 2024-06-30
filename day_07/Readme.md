# 🔥 Week 1 🔥 | Grand Challenge | Personal Finance Manager

## Description:
Create a Personal Finance Manager that helps users track their income, expenses, and savings. The system should support the following operations:
1. **Add a Transaction**:
    - Prompt the user for transaction details (date, description, amount, type [income/expense]).
    - Store the details in a dictionary and add it to the list of transactions.

2. **View Transactions**:
    - Display all transactions or filter by a specified date range.
    - Use formatted output to display the transactions.

3. **View Summary**:
    - Calculate and display the total income, total expenses, and net savings.

4. **Search Transactions**:
    - Allow the user to search for a transaction by description or amount.
    - Display the matching transactions if found.

5. **Save and Load Data**:
    - Save the transaction records to a file.
    - Load the transaction records from a file.

6. **Custom Module (`finance_utils.py`)**:
    - Implement utility functions for common tasks (e.g., input validation, date formatting). Develop the module by yourself

7. **Error Handling**:
    - Handle errors gracefully using try-except blocks.

## Example Output
```python
1. Add a new transaction
2. View transactions
3. View summary
4. Search for a transaction
5. Save data to file
6. Load data from file
7. Exit

Enter your choice: 1
Enter date (YYYY-MM-DD): 2024-06-28
Enter description: Salary
Enter amount: 5000
Enter type (income/expense): income

Transaction added successfully!
...

1. Add a new transaction
2. View transactions
3. View summary
4. Search for a transaction
5. Save data to file
6. Load data from file
7. Exit

Enter your choice: 2
View transactions from date (YYYY-MM-DD) or press Enter to view all: 
Transactions:
Date: 2024-06-28, Description: Salary, Amount: 5000, Type: income
Date: 2024-07-01, Description: Rent, Amount: 1500, Type: expense
Date: 2024-07-02, Description: Groceries, Amount: 300, Type: expense

1. Add a new transaction
2. View transactions
3. View summary
4. Search for a transaction
5. Save data to file
6. Load data from file
7. Exit

Enter your choice: 3
Summary:
Total Income: $5000
Total Expenses: $1800
Net Savings: $3200

1. Add a new transaction
2. View transactions
3. View summary
4. Search for a transaction
5. Save data to file
6. Load data from file
7. Exit

Enter your choice: 4
Enter description or amount to search: Rent
Search Results:
Date: 2024-07-01, Description: Rent, Amount: 1500, Type: expense

1. Add a new transaction
2. View transactions
3. View summary
4. Search for a transaction
5. Save data to file
6. Load data from file
7. Exit

Enter your choice: 5
Data saved successfully!

1. Add a new transaction
2. View transactions
3. View summary
4. Search for a transaction
5. Save data to file
6. Load data from file
7. Exit

Enter your choice: 6
Data loaded successfully!

1. Add a new transaction
2. View transactions
3. View summary
4. Search for a transaction
5. Save data to file
6. Load data from file
7. Exit

Enter your choice: 7
Exiting the system. Goodbye!
```