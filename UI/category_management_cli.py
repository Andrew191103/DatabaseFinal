import category_management as cm

def main():
    print("Welcome to the Category Management System!")

    while True:
        print("\nOptions:")
        print("1. Add Category")
        print("2. Update Category")
        print("3. Delete Category")
        print("4. View Category")
        print("5. View All Categories")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_category()
        elif choice == '2':
            update_category()
        elif choice == '3':
            delete_category()
        elif choice == '4':
            view_category()
        elif choice == '5':
            view_all_categories()
        elif choice == '6':
            print("Exiting the Category Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_category():
    category_name = input("Enter the name of the new category: ")
    category_id = cm.add_category(category_name)
    print(f"Category '{category_name}' added with ID: {category_id}")

def update_category():
    category_id = int(input("Enter the ID of the category to update: "))
    new_name = input("Enter the new name for the category: ")
    cm.update_category(category_id, new_name)
    print("Category updated successfully.")

def delete_category():
    category_id = int(input("Enter the ID of the category to delete: "))
    cm.delete_category(category_id)
    print("Category deleted successfully.")

def view_category():
    category_id = int(input("Enter the ID of the category to view: "))
    category = cm.get_category(category_id)
    if category:
        print(f"Category ID: {category[0]}, Name: {category[1]}")
    else:
        print("Category not found.")

def view_all_categories():
    categories = cm.get_all_categories()
    if categories:
        print("\nAll Categories:")
        for category in categories:
            print(f"ID: {category[0]}, Name: {category[1]}")
    else:
        print("No categories found.")

if __name__ == "__main__":
    main()
