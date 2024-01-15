import user_management

# Test adding a user
def test_add_user():
    username = "tank101"
    first_name = "gervonta"
    last_name = "davis"
    email = "gervontadavis@email.com"
    dob = "1990-01-01"
    gender = "Male"
    registration = "2024-01-01 10:00:00"
    shipping_address = "123 Test Lane"
    user_type = 1
    password = "aintnosafety"

    print("Testing: Adding a new user...")
    user_management.add_user(username, first_name, last_name, email, dob, gender, registration, shipping_address, user_type, password)
    print("Test add user completed.\n")

# Test fetching a user by username
def test_fetch_user_by_username():
    username = "baglover1"
    print(f"Testing: Fetching user by username '{username}'...")
    user = user_management.fetch_user_by_username(username)
    print("Fetched User:", user)
    print("Test fetch user by username completed.\n")

# Test verifying user login
def test_verify_user():
    username = "fashionista"
    password = "naoya"
    print(f"Testing: Verifying user login for '{username}'...")
    verification_result = user_management.verify_user(username, password)
    print("User verified:", verification_result)
    print("Test verify user completed.\n")

# Run the tests
if __name__ == "__main__":
    test_add_user()
    test_fetch_user_by_username()
    test_verify_user()
