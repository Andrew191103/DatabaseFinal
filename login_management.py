# login_management.py
import sql_queries
from werkzeug.security import check_password_hash, generate_password_hash

def authenticate_user(username, plaintext_password):
    user = sql_queries.fetch_user_by_username(username)
    if user:
        # Assuming 'Password' is the last element in the tuple
        hashed_password = user[-1]  # or the specific index of the Password column in your query
        if check_password_hash(hashed_password, plaintext_password):
            return True, user
    return False, None

def register_user(username, plaintext_password, email, first_name, last_name, dob, gender, registration, shipping_address, user_type):
    hashed_password = hash_password(plaintext_password)
    register_data = (username, first_name, last_name, email, dob, gender, registration, shipping_address, user_type, hashed_password)
    sql_queries.add_user(register_data)
    print("User registered successfully.")

def hash_password(password):
    return generate_password_hash(password)
