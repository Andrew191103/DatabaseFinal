import admin_level_management

def test_add_admin_level():
    print("Testing: Adding a new admin level...")
    admin_level_name = "New Level"  # Replace with the name you wish to add
    access_level_id = admin_level_management.add_admin_level(admin_level_name)
    print(f"Added new admin level with ID: {access_level_id}\n")

def test_update_admin_level():
    print("Testing: Updating an existing admin level...")
    admin_level_id = 1  # Replace with a valid ID
    new_name = "Updated Level Name"  # New name for the admin level
    admin_level_management.update_admin_level(admin_level_id, new_name)
    print(f"Updated admin level {admin_level_id} to new name: {new_name}\n")

#def test_delete_admin_level():
   # print("Testing: Deleting an admin level...")
    #admin_level_id = 1  # Replace with a valid ID to delete
    #admin_level_management.delete_admin_level(admin_level_id)
    #print(f"Deleted admin level with ID: {admin_level_id}\n")

def test_get_admin_level():
    print("Testing: Getting an admin level...")
    admin_level_id = 1 # Replace with a valid ID to retrieve
    admin_level = admin_level_management.get_admin_level(admin_level_id)
    print(f"Retrieved admin level: {admin_level}\n")

def test_get_all_admin_levels():
    print("Testing: Getting all admin levels...")
    all_admin_levels = admin_level_management.get_all_admin_levels()
    for level in all_admin_levels:
        print(f"Admin Level ID: {level[0]}, Name: {level[1]}")
    print()

# Uncomment the tests you wish to run
if __name__ == "__main__":
    test_add_admin_level()
    test_get_admin_level()
    test_update_admin_level()
    # test_delete_admin_level() # Caution: this will delete the admin level
    test_get_all_admin_levels()
