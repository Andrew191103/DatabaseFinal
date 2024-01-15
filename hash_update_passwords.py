# hash_update_passwords.py
from werkzeug.security import generate_password_hash
import sql_queries  # This should be the module where you define your database connection and queries

def hash_and_update_passwords():
    conn = sql_queries.create_connection()
    if conn is not None:
        cursor = conn.cursor()
        
        # Select users without a hashed password
        cursor.execute("SELECT User_ID, Username FROM User WHERE Password IS NULL OR Password = ''")
        users = cursor.fetchall()

        for user_id, username in users:
            # Prompt for a new password or generate one
            new_password = input(f"Enter new password for user {username}: ")
            hashed_password = generate_password_hash(new_password)
            
            # Update the User table with the new hashed password
            query = "UPDATE User SET Password = %s WHERE User_ID = %s"
            cursor.execute(query, (hashed_password, user_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Passwords updated successfully.")

if __name__ == "__main__":
    hash_and_update_passwords()
