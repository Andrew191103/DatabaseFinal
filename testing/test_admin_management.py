# test_admin_management.py
import admin_management

# This function tests the addition of a new admin to the database.
# It should create a new record in the Admin table.
def test_add_admin():
    print("Testing: Adding a new admin...")
    username = "newadmin"
    password = "testing"  # This should be a hashed password before being inserted into the database.
    email_address = "newadmin@example.com"
    access_level = 1  # Assuming '1' is a valid access level in your system.
    
    admin_management.add_admin(username, password, email_address, access_level)
    print("Test add admin completed.\n")

# This function tests the retrieval of an admin's details from the database.
# It should fetch a record from the Admin table based on the provided admin_id.
def test_fetch_admin():
    admin_id = 101  # Replace with a valid admin_id from your Admin table.
    print(f"Testing: Fetching admin by ID '{admin_id}'...")
    admin = admin_management.fetch_admin(admin_id)
    print("Fetched Admin:", admin)
    print("Test fetch admin completed.\n")

# This function tests the updating of an admin's details in the database.
# It should update a record in the Admin table based on the provided admin_id.
def test_update_admin():
    admin_id = 101  # Replace with a valid admin_id from your Admin table.
    username = "updatedadmin"
    password = "updatedpassword"  # This should be a hashed password before being updated in the database.
    email_address = "updatedadmin@example.com"
    access_level = 2  # Update with a new access level if necessary.
    
    print("Testing: Updating admin...")
    admin_management.update_admin(admin_id, username, password, email_address, access_level)
    print("Test update admin completed.\n")

# This function tests the deletion of an admin from the database.
# It should remove a record from the Admin table based on the provided admin_id.
def test_delete_admin():
    admin_id = 103  # Replace with a valid admin_id from your Admin table you wish to delete.
    print(f"Testing: Deleting admin with ID '{admin_id}'...")
    admin_management.delete_admin(admin_id)
print("Test delete admin completed.\n")

if __name__ == "__main__":
    test_add_admin() # Calls the function to test adding a new admin.
    test_fetch_admin() # Calls the function to test fetching an admin's details.
    test_update_admin() # Calls the function to test updating an admin's details.
# test_delete_admin() # Uncomment this line to perform the test.
