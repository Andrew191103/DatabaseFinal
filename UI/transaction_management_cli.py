import transaction_management as tm

def main():
    print("Welcome to the Transaction Management System!")

    while True:
        print("\nOptions:")
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View All Transactions")
        print("5. View Transaction by ID")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            update_transaction()
        elif choice == '3':
            delete_transaction()
        elif choice == '4':
            view_all_transactions()
        elif choice == '5':
            view_transaction_by_id()
        elif choice == '6':
            print("Exiting the Transaction Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_transaction():
    user_id = int(input("Enter the user ID: "))
    total_price = float(input("Enter the total price: "))
    status = input("Enter the status: ")
    admin_id = int(input("Enter the admin ID: "))
    transaction_time = input("Enter the transaction time (YYYY-MM-DD HH:MM:SS): ")

    tm.add_transaction(user_id, total_price, status, admin_id, transaction_time)
    print("Transaction added successfully.")

def update_transaction():
    order_id = int(input("Enter the transaction ID to update: "))
    user_id = int(input("Enter the new user ID: "))
    total_price = float(input("Enter the new total price: "))
    status = input("Enter the new status: ")
    admin_id = int(input("Enter the new admin ID: "))
    transaction_time = input("Enter the new transaction time (YYYY-MM-DD HH:MM:SS): ")

    updated_data = (user_id, total_price, status, admin_id, transaction_time)
    tm.update_transaction(order_id, updated_data)
    print("Transaction updated successfully.")

def delete_transaction():
    order_id = int(input("Enter the transaction ID to delete: "))
    tm.delete_transaction(order_id)
    print("Transaction deleted successfully.")

def view_all_transactions():
    transactions = tm.fetch_all_transactions()
    
    if transactions:
        print("\nAll Transactions:")
        for transaction in transactions:
            print(f"Transaction ID: {transaction[0]}")
            print(f"User ID: {transaction[1]}")
            print(f"Total Price: {transaction[2]}")
            print(f"Status: {transaction[3]}")
            print(f"Admin ID: {transaction[4]}")
            print(f"Transaction Time: {transaction[5]}")
    else:
        print("No transactions found.")

def view_transaction_by_id():
    order_id = int(input("Enter the transaction ID to view details: "))
    transaction = tm.fetch_transaction(order_id)
    
    if transaction:
        print("\nTransaction Details:")
        print(f"Transaction ID: {transaction[0]}")
        print(f"User ID: {transaction[1]}")
        print(f"Total Price: {transaction[2]}")
        print(f"Status: {transaction[3]}")
        print(f"Admin ID: {transaction[4]}")
        print(f"Transaction Time: {transaction[5]}")
    else:
        print("No transaction found for the provided ID.")

if __name__ == "__main__":
    main()
