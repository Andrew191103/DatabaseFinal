import mysql.connector
from mysql.connector import Error

# Database connection information
host = "localhost"
user = "root"
password = ""
database = "Official Reseller Management System"

# Function to create a database connection
def create_connection():
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None

# Function to add a new user
def add_user(user_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = ("INSERT INTO User "
             "(Username, First_Name, Last_Name, Email_Address, Date_of_Birth, "
             "Gender, Registration, Shipping_Address, user_type, Password) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(query, user_data)
        conn.commit()
        cursor.close()
        conn.close()

# Function to update a user
def update_user(user_id, updated_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "UPDATE User SET Username = %s, First_Name = %s, Last_Name = %s, Email_Address = %s, Date_of_Birth = %s, Gender = %s, Registration = %s, Shipping_Address = %s, user_type = %s WHERE User_ID = %s"
        cursor.execute(query, updated_data + (user_id,))
        conn.commit()
        cursor.close()
        conn.close()

# Function to delete a user
def delete_user(user_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "DELETE FROM User WHERE User_ID = %s"
        cursor.execute(query, (user_id,))
        conn.commit()
        cursor.close()
        conn.close()

# Function to fetch all users
def fetch_users():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM User"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users

# Function to fetch a specific user by ID
def fetch_user(user_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM User WHERE User_ID = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

# Function to fetch a user by username
def fetch_user_by_username(username):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM User WHERE Username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

# Function to add a product
def add_product(product_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = ("INSERT INTO Product "
                 "(Product_Name, Product_Price, Product_Description, Release_Date, "
                 "Product_Quantity, Category_ID, Stock_Quantity, Restock_Threshold, Last_Restocked) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(query, product_data)
        conn.commit()
        cursor.close()
        conn.close()

# Function to update a product
def update_product(updated_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = ("UPDATE Product SET "
                 "Product_Name = %s, Product_Price = %s, Product_Description = %s, Release_Date = %s, "
                 "Product_Quantity = %s, Category_ID = %s, Stock_Quantity = %s, Restock_Threshold = %s, Last_Restocked = %s "
                 "WHERE Product_ID = %s")
        cursor.execute(query, updated_data)
        conn.commit()
        cursor.close()
        conn.close()

# Function to delete a product
def delete_product(product_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "DELETE FROM Product WHERE Product_ID = %s"
        cursor.execute(query, (product_id,))
        conn.commit()
        cursor.close()
        conn.close()

# Function to fetch all products
def fetch_products():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Product"
        cursor.execute(query)
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products

# Function to fetch a specific product by ID
def fetch_product(product_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Product WHERE Product_ID = %s"
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()
        cursor.close()
        conn.close()
        return product
    
def add_transaction(transaction_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = ("INSERT INTO Transaction "
                 "(User_ID, Total_Price, Status, Admin_ID, transaction_time) "
                 "VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(query, transaction_data)
        conn.commit()
        cursor.close()
        conn.close()

def update_transaction(transaction_id, updated_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = ("UPDATE Transaction SET "
                 "User_ID = %s, Total_Price = %s, Status = %s, Admin_ID = %s, transaction_time = %s "
                 "WHERE Order_ID = %s")
        cursor.execute(query, updated_data + (transaction_id,))
        conn.commit()
        cursor.close()
        conn.close()

def delete_transaction(transaction_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "DELETE FROM Transaction WHERE Order_ID = %s"
        cursor.execute(query, (transaction_id,))
        conn.commit()
        cursor.close()
        conn.close()

def fetch_transactions():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Transaction"
        cursor.execute(query)
        transactions = cursor.fetchall()
        cursor.close()
        conn.close()
        return transactions

def fetch_transaction(transaction_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Transaction WHERE Order_ID = %s"
        cursor.execute(query, (transaction_id,))
        transaction = cursor.fetchone()
        cursor.close()
        conn.close()
        return transaction
    
def add_admin(admin_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        # The SQL query should match the columns in your Admin table.
        query = ("INSERT INTO Admin (Username, Password, Email_Address, Access_Level) "
                 "VALUES (%s, %s, %s, %s)")
        cursor.execute(query, admin_data)
        conn.commit()
        cursor.close()
        conn.close()

def update_admin(admin_id, updated_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = ("UPDATE Admin SET "
                 "Username = %s, Password = %s, Email_Address = %s, Access_Level = %s "
                 "WHERE Admin_ID = %s")
        cursor.execute(query, updated_data + (admin_id,))
        conn.commit()
        cursor.close()
        conn.close()

def delete_admin(admin_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "DELETE FROM Admin WHERE Admin_ID = %s"
        cursor.execute(query, (admin_id,))
        conn.commit()
        cursor.close()
        conn.close()

def fetch_admins():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Admin"
        cursor.execute(query)
        admins = cursor.fetchall()
        cursor.close()
        conn.close()
        return admins

def fetch_admin(admin_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Admin WHERE Admin_ID = %s"
        cursor.execute(query, (admin_id,))
        admin = cursor.fetchone()
        cursor.close()
        conn.close()
        return admin
    
def add_transaction_detail(transaction_detail_data):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = """
        INSERT INTO Transaction_Details (Transaction_ID, Product_ID, Product_Quantity, Unit_Price) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, transaction_detail_data)
        conn.commit()
        cursor.close()
        conn.close()

def update_transaction_detail(transaction_details_id, transaction_id, product_id, product_quantity, unit_price):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = """
        UPDATE Transaction_Details 
        SET Transaction_ID = %s, Product_ID = %s, Product_Quantity = %s, Unit_Price = %s 
        WHERE Transaction_Details_ID = %s
        """
        # Make sure the order of the parameters matches the placeholders in the SQL query
        cursor.execute(query, (transaction_id, product_id, product_quantity, unit_price, transaction_details_id))
        conn.commit()
        cursor.close()
        conn.close()

def delete_transaction_detail(transaction_details_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "DELETE FROM Transaction_Details WHERE Transaction_Details_ID = %s"
        cursor.execute(query, (transaction_details_id,))
        conn.commit()
        cursor.close()
        conn.close()

def fetch_transaction_details(transaction_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Transaction_Details WHERE Transaction_ID = %s"
        cursor.execute(query, (transaction_id,))
        details = cursor.fetchall()
        cursor.close()
        conn.close()
        return details
    
def add_category(category_name):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "INSERT INTO Category (Category_Name) VALUES (%s)"
        cursor.execute(query, (category_name,))
        conn.commit()
        cursor.close()
        conn.close()

def update_category(category_id, new_name):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "UPDATE Category SET Category_Name = %s WHERE Category_ID = %s"
        cursor.execute(query, (new_name, category_id))
        conn.commit()
        cursor.close()
        conn.close()

def delete_category(category_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "DELETE FROM Category WHERE Category_ID = %s"
        cursor.execute(query, (category_id,))
        conn.commit()
        cursor.close()
        conn.close()

def fetch_category(category_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Category WHERE Category_ID = %s"
        cursor.execute(query, (category_id,))
        category = cursor.fetchone()
        cursor.close()
        conn.close()
        return category

def fetch_all_categories():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Category"
        cursor.execute(query)
        categories = cursor.fetchall()
        cursor.close()
        conn.close()
        return categories
    
# Function to add a new admin level to the database
def add_admin_level(admin_level_name):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "INSERT INTO Admin_Level (Access_Level_Name) VALUES (%s)"
        cursor.execute(query, (admin_level_name,))
        conn.commit()
        admin_level_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return admin_level_id

# Function to update an existing admin level
def update_admin_level(admin_level_id, new_name):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "UPDATE Admin_Level SET Access_Level_Name = %s WHERE Access_Level_ID = %s"
        cursor.execute(query, (new_name, admin_level_id))
        conn.commit()
        cursor.close()
        conn.close()

# Function to delete an admin level
def delete_admin_level(admin_level_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "DELETE FROM Admin_Level WHERE Access_Level_ID = %s"
        cursor.execute(query, (admin_level_id,))
        conn.commit()
        cursor.close()
        conn.close()

# Function to fetch a single admin level by ID
def fetch_admin_level(admin_level_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Admin_Level WHERE Access_Level_ID = %s"
        cursor.execute(query, (admin_level_id,))
        admin_level = cursor.fetchone()
        cursor.close()
        conn.close()
        return admin_level

# Function to fetch all admin levels
def fetch_all_admin_levels():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM Admin_Level"
        cursor.execute(query)
        admin_levels = cursor.fetchall()
        cursor.close()
        conn.close()
        return admin_levels
    
def add_client_type(type_detail):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "INSERT INTO client_type (type_detail) VALUES (%s)"
        cursor.execute(query, (type_detail,))
        conn.commit()
        type_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return type_id

def update_client_type(type_id, new_type_detail):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "UPDATE client_type SET type_detail = %s WHERE type_id = %s"
        cursor.execute(query, (new_type_detail, type_id))
        conn.commit()
        cursor.close()
        conn.close()

def delete_client_type(type_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "DELETE FROM client_type WHERE type_id = %s"
        cursor.execute(query, (type_id,))
        conn.commit()
        cursor.close()
        conn.close()

def fetch_client_type(type_id):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT * FROM client_type WHERE type_id = %s"
        cursor.execute(query, (type_id,))
        client_type = cursor.fetchone()
        cursor.close()
        conn.close()
        return client_type

def fetch_all_client_types():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM client_type")
        client_types = cursor.fetchall()
        cursor.close()
        conn.close()
        return client_types