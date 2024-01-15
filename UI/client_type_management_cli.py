import client_type_management as ctm

def main():
    print("Welcome to the Client Type Management System!")

    while True:
        print("\nOptions:")
        print("1. Add Client Type")
        print("2. Update Client Type")
        print("3. Delete Client Type")
        print("4. View Client Type")
        print("5. View All Client Types")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_client_type()
        elif choice == '2':
            update_client_type()
        elif choice == '3':
            delete_client_type()
        elif choice == '4':
            view_client_type()
        elif choice == '5':
            view_all_client_types()
        elif choice == '6':
            print("Exiting the Client Type Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_client_type():
    type_detail = input("Enter the details of the new client type: ")
    type_id = ctm.add_client_type(type_detail)
    print(f"Client Type '{type_detail}' added with ID: {type_id}")

def update_client_type():
    type_id = int(input("Enter the ID of the client type to update: "))
    new_type_detail = input("Enter the new details for the client type: ")
    ctm.update_client_type(type_id, new_type_detail)
    print("Client Type updated successfully.")

def delete_client_type():
    type_id = int(input("Enter the ID of the client type to delete: "))
    ctm.delete_client_type(type_id)
    print("Client Type deleted successfully.")

def view_client_type():
    type_id = int(input("Enter the ID of the client type to view: "))
    client_type = ctm.get_client_type(type_id)
    if client_type:
        print(f"Client Type ID: {client_type[0]}, Details: {client_type[1]}")
    else:
        print("Client Type not found.")

def view_all_client_types():
    client_types = ctm.get_all_client_types()
    if client_types:
        print("\nAll Client Types:")
        for client_type in client_types:
            print(f"ID: {client_type[0]}, Details: {client_type[1]}")
    else:
        print("No client types found.")

if __name__ == "__main__":
    main()
