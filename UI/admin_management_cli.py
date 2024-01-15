import admin_management as am

def main():
    print("Welcome to the Admin Management System!")
    while True:
        print("\nOptions:")
        print("1. Add Admin")
        print("2. Update Admin")
        print("3. Delete Admin")
        print("4. View All Admins")
        print("5. View Admin by ID")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_admin()
        elif choice == '2':
            update_admin()
        elif choice == '3':
            delete_admin()
        elif choice == '4':
            view_all_admins()
        elif choice == '5':
            view_admin_by_id()
        elif choice == '6':
            print("Exiting the Admin Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_admin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email_address = input("Enter email address: ")
    access_level = input("Enter access level: ")
    am.add_admin(username, password, email_address, access_level)
    print("Admin added successfully.")

def update_admin():
    admin_id = input("Enter the ID of the admin to update: ")
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    email_address = input("Enter new email address: ")
    access_level = input("Enter new access level: ")
    am.update_admin(admin_id, username, password, email_address, access_level)
    print(f"Admin with ID {admin_id} updated successfully.")

def delete_admin():
    admin_id = input("Enter the ID of the admin to delete: ")
    am.delete_admin(admin_id)
    print(f"Admin with ID {admin_id} deleted successfully.")

def view_all_admins():
    admins = am.fetch_all_admins()
    print("\nAll Admins:")
    for admin in admins:
        print(f"ID: {admin[0]}, Username: {admin[1]}, Email: {admin[2]}, Access Level: {admin[3]}")

def view_admin_by_id():
    admin_id = input("Enter the ID of the admin to view: ")
    admin = am.fetch_admin(admin_id)
    if admin:
        print(f"\nAdmin ID: {admin[0]}")
        print(f"Username: {admin[1]}")
        print(f"Email: {admin[2]}")
        print(f"Access Level: {admin[3]}")
    else:
        print(f"No admin found with ID {admin_id}.")

if __name__ == "__main__":
    main()
