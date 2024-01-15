import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Successfully connected to the database")
        return conn
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None

def test_fetch_data():
    # Replace these with your actual database credentials and database name
    host_name = "localhost"
    user_name = "root"
    user_password = ""  # Your MySQL password
    db_name = "Official Reseller Management System"  # Your database name

    conn = create_connection(host_name, user_name, user_password, db_name)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product LIMIT 1")  # Ensure table name is correct
        result = cursor.fetchone()
        print(result)
        cursor.close()
        conn.close()

# Call the test function
test_fetch_data()