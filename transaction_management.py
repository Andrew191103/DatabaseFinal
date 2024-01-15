# transaction_management.py
import sql_queries

def add_transaction(user_id, total_price, status, admin_id, transaction_time):
    transaction_data = (user_id, total_price, status, admin_id, transaction_time)
    sql_queries.add_transaction(transaction_data)
    print("Transaction added successfully.")

def update_transaction(order_id, updated_data):
    sql_queries.update_transaction(order_id, updated_data)
    print("Transaction updated successfully.")

def delete_transaction(order_id):
    sql_queries.delete_transaction(order_id)
    print("Transaction deleted successfully.")

def fetch_all_transactions():
    return sql_queries.fetch_transactions()

def fetch_transaction(order_id):
    return sql_queries.fetch_transaction(order_id)
