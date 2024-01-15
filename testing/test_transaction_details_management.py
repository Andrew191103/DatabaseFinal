import transaction_details_management

#will add a new transaction detail record.
def test_add_transaction_detail():
    print("Testing: Adding a new transaction detail...")
    transaction_id = 10003  # Replace with a valid transaction_id
    product_id = 1001       # Replace with a valid product_id
    product_quantity = 1
    unit_price = 130        # This should be the price per unit of the product

    transaction_details_management.add_transaction_detail(transaction_id, product_id, product_quantity, unit_price)
    print("Test add transaction detail completed.\n")

#will retrieve the details for a given transaction.
def test_fetch_transaction_details():
    transaction_id = 10001  # Replace with a valid transaction_id
    print(f"Testing: Fetching transaction details for transaction ID '{transaction_id}'...")
    details = transaction_details_management.fetch_transaction_details(transaction_id)
    print("Fetched Transaction Details:", details)
    print("Test fetch transaction details completed.\n")

#will update a transaction detail record.
def test_update_transaction_detail():
    # Assuming you have a valid transaction_details_id from a previous add or from your data
    transaction_details_id = 100001  # Replace with a valid ID
    transaction_id = 10001           # Replace with a valid transaction_id
    product_id = 1001                # Replace with a valid product_id
    product_quantity = 2             # The new quantity you want to set
    unit_price = 135                 # The new unit price you want to set

    print("Testing: Updating transaction detail...")
    transaction_details_management.update_transaction_detail(
        transaction_details_id, transaction_id, product_id, product_quantity, unit_price
    )
    print("Test update transaction detail completed.\n")

#will delete a transaction detail record.
def test_delete_transaction_detail():
    transaction_details_id = 100003  # Replace with a valid transaction_details_id you want to delete

    print(f"Testing: Deleting transaction detail ID '{transaction_details_id}'...")
    transaction_details_management.delete_transaction_detail(transaction_details_id)
    print("Test delete transaction detail completed.\n")

# Run the tests
if __name__ == "__main__":
    test_add_transaction_detail()
    test_fetch_transaction_details()
    test_update_transaction_detail()
    test_delete_transaction_detail()  # Be cautious with this one to avoid deleting important data