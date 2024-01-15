# test_transaction_management.py
import transaction_management

# Test adding a transaction
def test_add_transaction():
    print("Testing: Adding a new transaction...")
    user_id = 101  # Replace with a valid user_id
    total_price = 129.99
    status = 1
    admin_id = 101  # Replace with a valid admin_id
    transaction_time = "2023-02-15 08:00:00"
    
    transaction_management.add_transaction(user_id, total_price, status, admin_id, transaction_time)
    print("Test add transaction completed.\n")

# Test fetching a transaction by Order_ID
def test_fetch_transaction():
    order_id = 10001  # Replace with a valid order_id
    print(f"Testing: Fetching transaction by Order_ID '{order_id}'...")
    transaction = transaction_management.fetch_transaction(order_id)
    print("Fetched Transaction:", transaction)
    print("Test fetch transaction completed.\n")

# Test updating a transaction
# Note: You'll need the order_id of an existing transaction to test this function
def test_update_transaction():
    order_id = 10002  # Replace with a valid order_id
    updated_user_id = 101
    updated_total_price = 79.99
    updated_status = 1
    updated_admin_id = 102
    updated_transaction_time = "2023-02-16 11:30:00"

    print("Testing: Updating transaction...")
    updated_data = (updated_user_id, updated_total_price, updated_status, updated_admin_id, updated_transaction_time)
    transaction_management.update_transaction(order_id, updated_data)
    print("Test update transaction completed.\n")

def test_fetch_all_transactions():
    print("Testing: Fetching all transactions...")
    transactions = transaction_management.fetch_all_transactions()
    for transaction in transactions:
        print(transaction)
    print("Test fetch all transactions completed.\n")

# test_delete_transaction function
def test_delete_transaction():
    order_id = 10003  # Replace with a valid order_id to be deleted
    print(f"Testing: Deleting transaction with Order_ID '{order_id}'...")
    transaction_management.delete_transaction(order_id)
    print("Test delete transaction completed.\n")


# Run the tests
if __name__ == "__main__":
    test_add_transaction()
    test_fetch_transaction()
    test_update_transaction()
    test_fetch_all_transactions()
    # test_delete_transaction()  # Uncomment to test the delete functionality
