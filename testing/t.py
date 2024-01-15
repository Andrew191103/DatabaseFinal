import user_management

# Test data
username = "testuser"
password = "Test@1234"
hashed_password = user_management.generate_password_hash(password)
first_name = "Test"
last_name = "User"
email = "testuser@example.com"
dob = "1990-01-01"
gender = "Other"
registration = "2023-01-01 10:00:00"
shipping_address = "123 Test St"
user_type = 1

# Test adding a user
print("Testing: Adding a user...")
user_management.add_user(username, first_name, last_name, email, dob, gender, registration, shipping_address, user_type, password)
print("User added.")

# Test fetching a user by username
print("Testing: Fetching a user by username...")
user = user_management.fetch_user_by_username(username)
print("Fetched User:", user)

# Assuming you know the user_id of the added user, replace 'user_id' with the actual ID
#user_id = user['101']  # Replace with the actual user ID obtained from the database

# Test updating a user
#print("Testing: Updating a user...")
#user_management.update_user(user_id, "new_username", "New", "Name", "newemail@example.com", dob, gender, registration, "456 New St", user_type)
#print("User updated.")

# Test fetching all users
print("Testing: Fetching all users...")
all_users = user_management.fetch_all_users()
print("All Users:", all_users)

# Test deleting a user
#print("Testing: Deleting a user...")
#user_management.delete_user(user_id)
#print("User deleted.")

# Test verifying user login
print("Testing: Verifying user login...")
login_success = user_management.verify_user(username, password)
print("Login success:", login_success)
