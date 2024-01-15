# user_management.py
import sql_queries
from werkzeug.security import generate_password_hash, check_password_hash

def add_user(username, first_name, last_name, email, dob, gender, registration, shipping_address, user_type, plain_text_password):
    hashed_password = generate_password_hash(plain_text_password)
    user_data = (username, first_name, last_name, email, dob, gender, registration, shipping_address, user_type, hashed_password)
    sql_queries.add_user(user_data)
    print("User added successfully.")

def update_user(username, first_name, last_name, email, dob, gender, registration, shipping_address, user_type, plain_text_password):
    hashed_password = generate_password_hash(plain_text_password)
    user_data = (username, first_name, last_name, email, dob, gender, registration, shipping_address, user_type, hashed_password)
    sql_queries.add_user(user_data)
    print("User updated successfully.")

def delete_user(user_id):
    sql_queries.delete_user(user_id)
    print("User deleted successfully.")

def fetch_all_users():
    return sql_queries.fetch_users()

def fetch_user(user_id):
    return sql_queries.fetch_user(user_id)

def fetch_user_by_username(username):
    return sql_queries.fetch_user_by_username(username)

def verify_user(username, plaintext_password):
    user = fetch_user_by_username(username)
    if user:
        # Assuming 'Password' is the last element in the tuple
        hashed_password = user[-1]  # or user[10] if it's the 11th column
        if check_password_hash(hashed_password, plaintext_password):
            return True  # User authenticated
    return False  # Authentication failed