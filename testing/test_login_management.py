import login_management

# Test registering a new user
def test_register_user():
    print("Testing: Registering a new user...")
    username = "bronzebomber9"
    password = "tillthisday"
    email = "deontaywilder3@example.com"
    first_name = "deontay"
    last_name = "wilder"
    dob = "1995-01-01"
    gender = "Male"
    registration = "2023-03-02 10:00:00"
    shipping_address = "34 Alabama"
    user_type = 1
    login_management.register_user(username, password, email, first_name, last_name, dob, gender, registration, shipping_address, user_type)
    print("Test register user completed.\n")

# Test authenticating a user
def test_authenticate_user():
    print("Testing: Authenticating a user...")
    username = "baglover1"
    password = "mayweather"
    authenticated, user = login_management.authenticate_user(username, password)
    print("User authenticated:", authenticated)
    print("Test authenticate user completed.\n")

# Run the tests
if __name__ == "__main__":
    test_register_user()
    test_authenticate_user()
