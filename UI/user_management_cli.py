import user_management as um
import getpass

def main():
    print("Welcome to the User Management System!")

    while True:
        print("\nOptions:")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. View All Users")
        print("5. View User by ID")
        print("6. Verify User")
        print("7. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            update_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            view_all_users()
        elif choice == '5':
            view_user_by_id()
        elif choice == '6':
            verify_user()
        elif choice == '7':
            print("Exiting the User Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_user():
    username = input("Enter the username: ")
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    email = input("Enter the email: ")
    dob = input("Enter the date of birth (YYYY-MM-DD): ")
    gender = input("Enter the gender: ")
    registration = input("Enter the registration details: ")
    shipping_address = input("Enter the shipping address: ")
    user_type = input("Enter the user type: ")
    plain_text_password = getpass.getpass("Enter the password: ")

    um.add_user(username, first_name, last_name, email, dob, gender, registration, shipping_address, user_type, plain_text_password)
    print("User added successfully.")

def update_user():
    # You can implement this function similarly to add_user but with updated data
    pass

def delete_user():
    user_id = int(input("Enter the user ID to delete: "))
    um.delete_user(user_id)
    print("User deleted successfully.")

def view_all_users():
    users = um.fetch_all_users()

    if users:
        print("\nAll Users:")
        for user in users:
            print(f"User ID: {user[0]}")
            print(f"Username: {user[1]}")
            print(f"First Name: {user[2]}")
            print(f"Last Name: {user[3]}")
            print(f"Email: {user[4]}")
            print(f"Date of Birth: {user[5]}")
            print(f"Gender: {user[6]}")
            print(f"Registration: {user[7]}")
            print(f"Shipping Address: {user[8]}")
            print(f"User Type: {user[9]}")
    else:
        print("No users found.")

def view_user_by_id():
    user_id = int(input("Enter the user ID to view details: "))
    user = um.fetch_user(user_id)

    if user:
        print("\nUser Details:")
        print(f"User ID: {user[0]}")
        print(f"Username: {user[1]}")
        print(f"First Name: {user[2]}")
        print(f"Last Name: {user[3]}")
        print(f"Email: {user[4]}")
        print(f"Date of Birth: {user[5]}")
        print(f"Gender: {user[6]}")
        print(f"Registration: {user[7]}")
        print(f"Shipping Address: {user[8]}")
        print(f"User Type: {user[9]}")
    else:
        print("No user found for the provided ID.")

def verify_user():
    username = input("Enter the username: ")
    plain_text_password = getpass.getpass("Enter the password: ")

    if um.verify_user(username, plain_text_password):
        print("User verified successfully.")
    else:
        print("User verification failed.")

if __name__ == "__main__":
    main()
