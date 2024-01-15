# transaction_details_management.py
import sql_queries

def add_transaction_detail(transaction_id, product_id, product_quantity, unit_price):
    transaction_detail_data = (transaction_id, product_id, product_quantity, unit_price)
    sql_queries.add_transaction_detail(transaction_detail_data)
    print("Transaction detail added successfully.")

def update_transaction_detail(transaction_details_id, transaction_id, product_id, product_quantity, unit_price):
    # Here, the updated_data should be passed as individual arguments, not as a single tuple
    sql_queries.update_transaction_detail(transaction_details_id, transaction_id, product_id, product_quantity, unit_price)
    
def delete_transaction_detail(transaction_details_id):
    sql_queries.delete_transaction_detail(transaction_details_id)
    print("Transaction detail deleted successfully.")

def fetch_transaction_details(transaction_id):
    details = sql_queries.fetch_transaction_details(transaction_id)
    return details
