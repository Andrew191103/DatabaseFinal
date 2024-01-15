import getpass
import login_management as lm

def main():
    print("Welcome to the Official Reseller Management System!")
    while True:
        print("\nOptions:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    authenticated, user = lm.authenticate_user(username, password)
    
    if authenticated:
        print("Login successful!")
        print("Welcome, " + user[1])  # Assuming First_Name is the second element in the user tuple
        # Add your logic for user actions after login here
    else:
        print("Login failed. Please check your username and password.")

def register():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    email = input("Enter your email: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    gender = input("Enter your gender: ")
    registration = input("Enter your registration details: ")
    shipping_address = input("Enter your shipping address: ")
    user_type = input("Enter your user type: ")

    lm.register_user(username, password, email, first_name, last_name, dob, gender, registration, shipping_address, user_type)
    
if __name__ == "__main__":
    main()
