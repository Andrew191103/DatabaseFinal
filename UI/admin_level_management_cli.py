import admin_level_management as alm

def main():
    print("Welcome to the Admin Level Management System!")

    while True:
        print("\nOptions:")
        print("1. Add Admin Level")
        print("2. Update Admin Level")
        print("3. Delete Admin Level")
        print("4. View All Admin Levels")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_admin_level()
        elif choice == '2':
            update_admin_level()
        elif choice == '3':
            delete_admin_level()
        elif choice == '4':
            view_all_admin_levels()
        elif choice == '5':
            print("Exiting the Admin Level Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_admin_level():
    access_level_name = input("Enter the name of the new admin level: ")
    admin_level_id = alm.add_admin_level(access_level_name)
    print(f"Admin level '{access_level_name}' added with ID: {admin_level_id}")

def update_admin_level():
    access_level_id = int(input("Enter the ID of the admin level to update: "))
    new_name = input("Enter the new name for the admin level: ")
    alm.update_admin_level(access_level_id, new_name)
    print("Admin level updated successfully.")

def delete_admin_level():
    access_level_id = int(input("Enter the ID of the admin level to delete: "))
    alm.delete_admin_level(access_level_id)
    print("Admin level deleted successfully.")

def view_all_admin_levels():
    admin_levels = alm.get_all_admin_levels()
    if admin_levels:
        print("\nAll Admin Levels:")
        for level in admin_levels:
            print(f"ID: {level[0]}, Name: {level[1]}")
    else:
        print("No admin levels found.")

if __name__ == "__main__":
    main()
