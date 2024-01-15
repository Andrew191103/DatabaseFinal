# admin_management.py
import sql_queries
from werkzeug.security import generate_password_hash

def add_admin(username, password, email_address, access_level):
    # Hash the password before storing it in the database
    hashed_password = generate_password_hash(password)
    
    # Prepare the data for insertion
    admin_data = (username, hashed_password, email_address, access_level)
    
    # Call the function from sql_queries to add the admin
    sql_queries.add_admin(admin_data)
    print("Admin added successfully.")

def update_admin(admin_id, username, password, email_address, access_level):
    # Hash the new password before updating
    hashed_password = generate_password_hash(password)
    
    # Prepare the updated data
    updated_data = (username, hashed_password, email_address, access_level)
    
    # Call the function from sql_queries to update the admin
    sql_queries.update_admin(admin_id, updated_data)
    print("Admin updated successfully.")

def delete_admin(admin_id):
    # Call the function from sql_queries to delete the admin
    sql_queries.delete_admin(admin_id)
    print("Admin deleted successfully.")

def fetch_all_admins():
    # Call the function from sql_queries to fetch all admins
    admins = sql_queries.fetch_admins()
    return admins

def fetch_admin(admin_id):
    # Call the function from sql_queries to fetch a single admin by ID
    admin = sql_queries.fetch_admin(admin_id)
    return admin

# Additional functions related to admin management could be added here
