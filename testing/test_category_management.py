import category_management

def test_add_category():
    print("Testing: Adding a new category...")
    new_category_name = "Satchels"
    category_id = 504
    print(f"New category added with ID: {category_id}")

def test_update_category():
    print("Testing: Updating category...")
    category_id = 502  # Use an existing category ID
    new_name = "Designer Backpacks"
    category_management.update_category(category_id, new_name)
    print("Category updated successfully.")

def test_delete_category():
    print("Testing: Deleting category...")
    category_id = 504  # Use an existing category ID that can be deleted
    category_management.delete_category(category_id)
    print("Category deleted successfully.")

def test_get_category():
    print("Testing: Fetching category...")
    category_id = 501  # Use an existing category ID
    category = category_management.get_category(category_id)
    print(f"Fetched Category: {category}")

def test_get_all_categories():
    print("Testing: Fetching all categories...")
    categories = category_management.get_all_categories()
    print(f"All Categories: {categories}")

# Run the tests
if __name__ == "__main__":
    test_add_category()
    test_update_category()
    test_delete_category()
    test_get_category()
    test_get_all_categories()
