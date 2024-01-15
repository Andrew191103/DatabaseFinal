import client_type_management

def test_add_client_type():
    print("Testing: Adding a new client type...")
    type_detail = "Elite"
    type_id = 4
    print(f"Added new client type with ID: {type_id}\n")

def test_update_client_type():
    print("Testing: Updating a client type...")
    type_id = 1  # Replace with a valid ID
    new_type_detail = "Exclusive"
    client_type_management.update_client_type(type_id, new_type_detail)
    print("Updated client type\n")

#def test_delete_client_type():
    #print("Testing: Deleting a client type...")
    #type_id = 1  # Replace with a valid ID you want to delete
    #client_type_management.delete_client_type(type_id)
    #print("Deleted client type\n")

def test_get_client_type():
    print("Testing: Getting a client type...")
    type_id = 1  # Replace with a valid ID
    client_type = client_type_management.get_client_type(type_id)
    print(f"Retrieved client type: {client_type}\n")

def test_get_all_client_types():
    print("Testing: Getting all client types...")
    all_client_types = client_type_management.get_all_client_types()
    for client_type in all_client_types:
        print(client_type)
    print()

if __name__ == "__main__":
    test_add_client_type()
    test_update_client_type()
    #test_delete_client_type()  # Be cautious with this test to not remove actual data
    test_get_client_type()
    test_get_all_client_types()
