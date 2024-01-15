import transaction_details_management as tdm

def main():
    print("Welcome to the Transaction Details Management System!")

    while True:
        print("\nOptions:")
        print("1. Add Transaction Detail")
        print("2. Update Transaction Detail")
        print("3. Delete Transaction Detail")
        print("4. View Transaction Details")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_transaction_detail()
        elif choice == '2':
            update_transaction_detail()
        elif choice == '3':
            delete_transaction_detail()
        elif choice == '4':
            view_transaction_details()
        elif choice == '5':
            print("Exiting the Transaction Details Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_transaction_detail():
    transaction_id = int(input("Enter the transaction ID: "))
    product_id = int(input("Enter the product ID: "))
    product_quantity = int(input("Enter the product quantity: "))
    unit_price = float(input("Enter the unit price: "))

    tdm.add_transaction_detail(transaction_id, product_id, product_quantity, unit_price)
    print("Transaction detail added successfully.")

def update_transaction_detail():
    transaction_details_id = int(input("Enter the transaction details ID to update: "))
    transaction_id = int(input("Enter the new transaction ID: "))
    product_id = int(input("Enter the new product ID: "))
    product_quantity = int(input("Enter the new product quantity: "))
    unit_price = float(input("Enter the new unit price: "))

    tdm.update_transaction_detail(transaction_details_id, transaction_id, product_id, product_quantity, unit_price)
    print("Transaction detail updated successfully.")

def delete_transaction_detail():
    transaction_details_id = int(input("Enter the transaction details ID to delete: "))
    tdm.delete_transaction_detail(transaction_details_id)
    print("Transaction detail deleted successfully.")

def view_transaction_details():
    transaction_id = int(input("Enter the transaction ID to view details: "))
    details = tdm.fetch_transaction_details(transaction_id)
    
    if details:
        print("\nTransaction Details:")
        for detail in details:
            print(f"Transaction Details ID: {detail[0]}")
            print(f"Transaction ID: {detail[1]}")
            print(f"Product ID: {detail[2]}")
            print(f"Product Quantity: {detail[3]}")
            print(f"Unit Price: {detail[4]}")
    else:
        print("No transaction details found for the provided transaction ID.")

if __name__ == "__main__":
    main()
