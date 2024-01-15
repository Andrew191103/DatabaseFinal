import product_management

# Test adding a product
def test_add_product():
    print("Testing: Adding a new product...")
    product_name = "Elegant Vase"
    product_price = 45.99
    product_description = "A beautifully crafted vase to complement your decor."
    release_date = "2024-01-14"
    product_quantity = 30
    category_id = 503  # Assuming this is a valid category in your Category table
    stock_quantity = 30
    restock_threshold = 5
    last_restocked = "2024-01-14 09:00:00"
    
    product_management.add_product(
        product_name, product_price, product_description, release_date,
        product_quantity, category_id, stock_quantity, restock_threshold, last_restocked
    )
    print("Test add product completed.\n")

# Test fetching a product by ID
def test_fetch_product():
    product_id = 1001  # Replace with a valid product_id
    print(f"Testing: Fetching product by ID '{product_id}'...")
    product = product_management.fetch_product(product_id)
    print("Fetched Product:", product)
    print("Test fetch product completed.\n")

# Test updating a product
# Note: You'll need the product_id of an existing product to test this function
def test_update_product():
    product_id = 1001  # Replace with a valid product_id
    updated_name = "Posh Pouches"
    updated_price = 49.99
    updated_description = "An updated description for the previously added vase."
    updated_release_date = "2024-02-01"
    updated_product_quantity = 25
    updated_category_id = 503  # Replace with the new category if needed
    updated_stock_quantity = 25
    updated_restock_threshold = 10
    updated_last_restocked = "2024-01-20 10:00:00"
    
    print("Testing: Updating product...")
    product_management.update_product(
        product_id, updated_name, updated_price, updated_description, updated_release_date,
        updated_product_quantity, updated_category_id, updated_stock_quantity, updated_restock_threshold, updated_last_restocked
    )
    print("Test update product completed.\n")

# Test deleting a product
# Note: Be cautious with this test to avoid removing real product data unintentionally
def test_delete_product():
    product_id = 1004  # Replace with a valid product_id to be deleted
    print(f"Testing: Deleting product with ID '{product_id}'...")
    product_management.delete_product(product_id)
    print("Test delete product completed.\n")

# Run the tests
if __name__ == "__main__":
    test_add_product()
    test_fetch_product()
    test_update_product()
    # Uncomment the next line to run the delete test when you are ready to actually delete a product
    # test_delete_product()

